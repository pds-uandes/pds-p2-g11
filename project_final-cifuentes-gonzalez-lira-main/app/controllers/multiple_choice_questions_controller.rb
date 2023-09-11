class MultipleChoiceQuestionsController < ApplicationController
  before_action :authenticate_user!

  def show
    @multiple_choice_question = MultipleChoiceQuestion.find(params[:id])
  end
end
