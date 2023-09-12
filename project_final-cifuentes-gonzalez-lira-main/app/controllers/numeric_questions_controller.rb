class NumericQuestionsController < ApplicationController
    # Redirect or render as needed
    def show
      @numeric_question = NumericQuestion.find(params[:id])
      @parameters = @numeric_question.parameters
      @user = current_user
      @task = @user.tasks.last
    end

    def submit_answer
      @numeric_question = NumericQuestion.find(params[:id])
      correct_answer = @numeric_question.numeric_answers.first

      user_answer = params[:answers][params[:id]]
      # user_answer = NumericAnswer.find(params[:answer])

      @user = current_user
      @task = @user.tasks.last

      is_correct = correct_answer.respuesta == user_answer

      # Add the question ID to the answered list
      @task.answered << @numeric_question.id
      @task.answered.uniq!

      if !is_correct
        # If the answer is incorrect, add the question ID to the wrongs list
        @task.wrongs << @numeric_question.id
        @task.wrongsaux << @numeric_question.id
        @task.wrongs.uniq!
        @task.wrongsaux.uniq!

      else
        @task.score += 1
        @task.wrongs.delete(@numeric_question.id)
      end

      @task.save

     next_question = @task.numeric_questions.where.not(id: @task.answered).sample

      if next_question
        redirect_to numeric_question_path(next_question)
      else
        # Handle the case where there are no more questions

        redirect_to results_path(task_id: @task.id)
      end
    end

end
