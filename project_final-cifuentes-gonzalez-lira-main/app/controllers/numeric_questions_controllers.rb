class NumericQuestionsController < ApplicationController
    # Redirect or render as needed


    def show
      @numeric_question = NumericQuestion.find(params[:id])
      @user = current_user
      @task = @user.tasks.last
    end


end
