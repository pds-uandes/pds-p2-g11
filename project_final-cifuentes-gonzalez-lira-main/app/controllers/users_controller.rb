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

    if @user.tasks.empty?
      # Create a new task with 3 random questions from the seed
      @task = Task.create(user: @user)
      questions = MultipleChoiceQuestion.where(topic: "TEMA 1").order("RANDOM()").limit(3)
      @task.multiple_choice_questions << questions
      puts @task
      if @task.save
        puts "Task saved successfully"
      else
        puts "Failed to save task"
        puts @task.errors.full_messages
      end

    else
      # Use the last task of the user
      @task = @user.tasks.last
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


  def redo_task

    puts "REDOOOOOOOOOOOOOOOOOOOOOOOOOO"

  end


end
