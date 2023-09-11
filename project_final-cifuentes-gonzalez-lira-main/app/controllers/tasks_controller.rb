class TasksController < ApplicationController
    # def start_task
    #     @user = current_user  # Get the current user

    #     if @user.tasks.empty?
    #       # Create a new task with 4 random questions
    #       @task = Task.create(user: @user)
    #       questions = MultipleChoiceQuestion.where(topic: "TEMA 1").sample(4)
    #       @task.questions = questions
    #       if @task.save
    #         puts "Task saved successfully"
    #       else
    #         puts "Failed to save task"
    #         puts @task.errors.full_messages
    #       end
    #     else
    #       # Use the last task of the user
    #       @task = @user.tasks.last
    #     end

    #     if @task&.multiple_choice_questions&.present?
    #       # Redirect to a random question from the task
    #       redirect_to multiple_choice_question_path(@task.multiple_choice_questions.sample)
    #     else
    #       # Handle the case where there are no questions or @task is nil
    #       # Redirect to an appropriate page or display an error message
    #       redirect_to root_path, alert: "No questions available for the task."
    #     end
    #   end

end
