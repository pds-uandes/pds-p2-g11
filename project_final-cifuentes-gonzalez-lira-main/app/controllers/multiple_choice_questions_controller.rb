class MultipleChoiceQuestionsController < ApplicationController
  before_action :authenticate_user!


  def show
    @multiple_choice_question = MultipleChoiceQuestion.find(params[:id])
  end

  def submit_answer
    @multiple_choice_question = MultipleChoiceQuestion.find(params[:id])
    selected_choice = Choice.find(params[:selected_choice])

    #Buscamos el task para actualizar el json/diccionario
    @task = @multiple_choice_question.task
    # Check if the answer is correct
    is_correct = selected_choice.correct?


    # Add the question ID to the answered list
    @task.answered << @multiple_choice_question.id
    @task.answered.uniq!

    unless is_correct
      # If the answer is incorrect, add the question ID to the wrongs list
      @task.wrongs << @multiple_choice_question.id
      @task.wrongs.uniq!
    end

    #Actualizamos el json del task
    @task.save

    # If the answer is correct, redirect to another question
    #next_question = @multiple_choice_question.task.multiple_choice_questions.where.not(id: @multiple_choice_question.id).sample
    next_question = @task.multiple_choice_questions.where.not(id: @task.answered).sample

    if next_question
      redirect_to multiple_choice_question_path(next_question)
    else
      # Handle the case where there are no more questions
      redirect_to results_path(@task)
      redirect_to root_path, notice: "You've answered all questions!"
    end
  end


end
