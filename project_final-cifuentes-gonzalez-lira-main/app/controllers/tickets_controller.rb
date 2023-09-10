class TicketsController < ApplicationController
    before_action :authenticate_user!
    before_action :ensure_normal_user, only: [:new]
  
    def index
      #Search functionality executive
      if params[:search] && current_user.executive?
        @tickets = current_user.executive_user_tickets.search(params[:search])
        respond_to do |format|
          format.html
          format.js { render partial: 'tickets/tickets_list', locals: { tickets: @tickets } }
        end
      #Supervisor and admin user
      elsif params[:search] && (current_user.admin? || current_user.supervisor?)
          @tickets = Ticket.search(params[:search])
          respond_to do |format|
            format.html
            format.js { render partial: 'tickets/tickets_list', locals: { tickets: @tickets } }
          end

          #Normal user
      elsif params[:search] && (current_user.normal?)
        @tickets = current_user.normal_user_tickets.search(params[:search])
        respond_to do |format|
          format.html
          format.js { render partial: 'tickets/tickets_list', locals: { tickets: @tickets } }
        end


        #Sort functionality
      elsif params[:sort_by] == 'priority' && current_user.executive?
        order = params[:order] || 'asc'
        @tickets = current_user.executive_user_tickets.order_by_priority(order)
      
      elsif params[:sort_by] == 'deadline' && current_user.executive?
        order = params[:order] || 'asc'
        @tickets = current_user.executive_user_tickets.order(deadline: order.to_sym)

      elsif params[:sort_by] == 'created_at' && current_user.normal?
          order = params[:order] || 'asc'
          @tickets = current_user.normal_user_tickets.order(created_at: order.to_sym)
      #Regular index functionality
      elsif params[:user_id]
        @user = User.find(params[:user_id])
        if @user.normal?
          @tickets = @user.normal_user_tickets
        elsif @user.executive?
          @tickets = @user.executive_user_tickets
        end
      elsif current_user.executive?
        @tickets = current_user.executive_user_tickets
      else
        @tickets = current_user.normal_user_tickets.order(created_at: :asc)
      end
    
      # @tickets.each(&:update_priority_based_on_deadline)
    end
    
    def overdue_ticket_report
      authorize! :read, :overdue_ticket_report
      @overdue_tickets = Ticket.where("state = ? AND deadline < ?", 0, Time.now).order(deadline: :desc)
    end

    def reports
      authorize! :read, :reports
      @ticket_counts = {}
      @tag_counts = {}
      months = Date::MONTHNAMES.compact
      months.each do |month|
        month_number = Date::MONTHNAMES.index(month)
        start_date = Date.new(Time.now.year, month_number).beginning_of_month
        end_date = Date.new(Time.now.year, month_number).end_of_month
        opened_tickets = Ticket.where(created_at: start_date..end_date).count
        closed_tickets = Ticket.where(closed_at: start_date..end_date).count
        if opened_tickets > 0 || closed_tickets > 0
          @ticket_counts[month] = { opened: opened_tickets, closed: closed_tickets }
          tags = Tag.joins(:tickets).where(tickets: { created_at: start_date..end_date }).group(:name).count
          @tag_counts[month] = tags
        end
      end
    end


    def executive_performance_report
      authorize! :read, :executive_performance_report
      @start_date = Date.today.beginning_of_year
      @end_date = Date.today.end_of_year
      @executives = User.executive.includes(:executive_user_tickets)
      @data = @executives.map do |executive|
        tickets = executive.executive_user_tickets.where(created_at: @start_date..@end_date)
        next if tickets.empty?
        closed_tickets = tickets.where.not(closed_at: nil)
        open_tickets = tickets.where(closed_at: nil)
        average_rating = closed_tickets.average(:response_quality) || 0
        
        {
          executive: executive,
          year: tickets.first.created_at.year,
          tickets_created: tickets.count,
          tickets_closed: closed_tickets.count,
          open_cases: open_tickets.count,
          average_rating: average_rating.round(2)
        }
      end.compact.group_by { |row| row[:year] }
    end

        
    
    

    def search
      @tickets = Ticket.where("title LIKE ?", "%#{params[:query]}%")
      render layout: false
    end
    
    def add_tag
      @ticket = Ticket.find(params[:id])
      tag = Tag.find_or_create_by(name: params[:name])
      @ticket.tags << tag
      redirect_to @ticket
    end
    
  
    def fill_executive_response(executive_user, response)
      if executive_user == self.executive_user
        self.executive_response = response
        self.save
      else
        # handle error case where executive_user is not authorized to fill in the response
      end
    end
  
    def edit
      begin
        @ticket = Ticket.find(params[:id])
      rescue ActiveRecord::RecordNotFound
        # handle error case where ticket with specified ID is not found
        redirect_to tickets_path, alert: "Ticket not found"
      end
    end
  

    def update
      @ticket = Ticket.find(params[:id])
      
      if params[:accept_response]
        @ticket.update(response_quality: params[:ticket][:response_quality], state: "closed", closed_at: Time.current)
        flash[:notice] = "Ticket solved successfully!"
        redirect_to @ticket
      elsif params[:reopen]
        @ticket.update(response_quality: params[:ticket][:response_quality], state: "reopened")
        flash[:notice] = "Ticket reopened successfully!"
        redirect_to @ticket
      elsif params[:submit_response]
        @ticket.update(executive_response: params[:ticket][:executive_response])
        flash[:notice] = "Response sent, waiting for user answer!"
        redirect_to @ticket
      elsif @ticket.update(ticket_params)
        flash[:notice] = "Ticket updated successfully!"
        redirect_to @ticket
      else
        render :edit
      end
      puts @ticket.errors.full_messages
    end
    
  
    def show
      @ticket = Ticket.find params[:id]
    end
  
    def new
      @ticket = Ticket.new
    end
  
    def create
      ticket = Ticket.new(ticket_params)
      ticket.normal_user = current_user
      ticket.state = :open
      ticket.priority = 'low'
      ticket.deadline = Time.now + 7.days
  
      executive = User.executive.left_joins(:executive_user_tickets).group(:id).order('COUNT(tickets.id) ASC').first
      ticket.executive_user = executive
  
      if ticket.save
        flash[:notice] = 'Ticket created successfully!'
        redirect_to ticket
      else
        puts "State after save: #{ticket.state}"
        puts ticket.errors.full_messages
        render :new
      end
    end
  
    def destroy
      ticket = Ticket.find params[:id]
      ticket.destroy
      flash[:notice] = 'Ticket deleted successfully!'
      redirect_to tickets_path
    end
  
   
    private
  
    def ticket_params
      params.require(:ticket).permit(:title, :description, :incident_date, :executive_response, :response_quality, :executive_user_id, :priority ,images: [])
    end
    
  
    def ensure_normal_user
      unless current_user.normal?
        redirect_to root_path, alert: 'Only normal users can create tickets'
      end
    end
  
  end 
  
