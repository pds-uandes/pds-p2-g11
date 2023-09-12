class ResultsController < ApplicationController
    def index
        @user = current_user
        @task = @user.tasks.last
        #@task = Task.find(params[:id]) # Find the task using the ID passed in params

        @questions = @task.multiple_choice_questions # Get all multiple choice questions associated with this task
        @wrong = @task.wrongs # Get all wrong questions associated with this task
        @task.redo = @wrong.empty?

        # Save the @task to persist the redo flag
        @task.save
    end
  end
