class UsersController < ApplicationController
  def show
      @user = User.find(params[:id])
  end

  before_action :authenticate_user!
  before_action :ensure_authorized_user, only: [:index]

  def index
    @normal_users = User.normal
    @executive_users = User.executive
    @supervisor_users = User.supervisor
    @admin_users = User.admin
  end

  def edit
      @user = User.find(params[:id])
  end

  def update
      @user = User.find(params[:id])
      if @user.update(user_params)
        redirect_to @user, notice: "User was successfully updated."
      else
        render :edit
      end
    end

  def user_params
    params.require(:user).permit(:role)
  end

  def ensure_authorized_user
    unless current_user.admin? || current_user.supervisor?
      redirect_to root_path, alert: 'You are not authorized to access this page'
    end
  end


  def start_task
    @user = current_user
    @user.tasks.destroy_all
    puts "Este usuario esta en el task numero:"
    puts @user.task
    puts "----------------------------------"

    puts "Este TIene este tasks"
    puts @user.tasks
    puts "----------------------------------"

    if @user.tasks.empty?

      if @user.task == 1

        @task = Task.create(user: @user, score: 0)
        # @task.numeric_questions << nq

        questions = NumericQuestion.where(topic: "TEMA 1").limit(1)
        if @task.save
          puts "Task saved successfully"
        else
          puts "Failed to save task"
          puts @task.errors.full_messages
        end

        puts "Esta es la pregunta numerica escogida:"
        puts questions.first.pregunta
        @task.numeric_questions << questions

        puts "Numeric question present???"
        puts @task&.numeric_questions&.present?
        puts "==================================="
        #redirect_to numeric_question_path(@task.numeric_questions.first)
        if @task&.numeric_questions&.present?
          # Redirect to the first question in the task
          #redirect_to multiple_choice_question_path(@task.multiple_choice_questions.first)
          #hacer redirect
          puts "-------------"
          redirect_to numeric_question_path(@task.numeric_questions.first)

          #redirect_to root_path, alert: "Redirect de numerical"
        else
          # Handle the case where there are no questions or @task is nil
          # Redirect to an appropriate page or display an error message
          redirect_to root_path, alert: "No questions available for the task."
          return
        end

      end#End de user.task = 1
      end

      if @user.task == 0
          # Create a new task with 3 random questions from the seed
          @task = Task.create(user: @user, score: 0)
          questions = MultipleChoiceQuestion.where(topic: "TEMA 1").order("RANDOM()").limit(3)
          @task.multiple_choice_questions << questions
          puts @task
          if @task.save
            puts "Task saved successfully"
          else
            puts "Failed to save task"
            puts @task.errors.full_messages
          end

        if @task&.multiple_choice_questions&.present?
          # Redirect to the first question in the task
          redirect_to multiple_choice_question_path(@task.multiple_choice_questions.first)
        else
          # Handle the case where there are no questions or @task is nil
          # Redirect to an appropriate page or display an error message
          redirect_to root_path, alert: "No questions available for the task."
        end
      end

      if @user.task == 2
        # Create a new task with 3 random questions from the seed
        @task = Task.create(user: @user, score: 0)
        questions = MultipleChoiceQuestion.where(topic: "TEMA 2").order("RANDOM()").limit(4)
        @task.multiple_choice_questions << questions
        puts @task
        if @task.save
          puts "Task saved successfully"
        else
          puts "Failed to save task"
          puts @task.errors.full_messages
        end

      if @task&.multiple_choice_questions&.present?
        # Redirect to the first question in the task
        redirect_to multiple_choice_question_path(@task.multiple_choice_questions.first)
      else
        # Handle the case where there are no questions or @task is nil
        # Redirect to an appropriate page or display an error message
        redirect_to root_path, alert: "No questions available for the task."
      end
    end

    if @user.task == 3

      @task = Task.create(user: @user, score: 0)
      # @task.numeric_questions << nq

      questions = NumericQuestion.where(topic: "TEMA 2").limit(1)
      if @task.save
        puts "Task saved successfully"
      else
        puts "Failed to save task"
        puts @task.errors.full_messages
      end

      puts "Esta es la pregunta numerica escogida:"
      puts questions.first.pregunta
      @task.numeric_questions << questions

      puts "Numeric question present???"
      puts @task&.numeric_questions&.present?
      puts "==================================="
      #redirect_to numeric_question_path(@task.numeric_questions.first)
      if @task&.numeric_questions&.present?
        # Redirect to the first question in the task
        #redirect_to multiple_choice_question_path(@task.multiple_choice_questions.first)
        #hacer redirect
        puts "-------------"
        redirect_to numeric_question_path(@task.numeric_questions.first)

        #redirect_to root_path, alert: "Redirect de numerical"
      else
        # Handle the case where there are no questions or @task is nil
        # Redirect to an appropriate page or display an error message
        redirect_to root_path, alert: "No questions available for the task."
        return
      end

    end#End de user.task = 1


    end
end
