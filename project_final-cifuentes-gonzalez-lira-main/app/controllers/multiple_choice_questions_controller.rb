class MultipleChoiceQuestionsController < ApplicationController
  before_action :authenticate_user!


  def show
    @multiple_choice_question = MultipleChoiceQuestion.find(params[:id])
    @user = current_user
    @task = @user.tasks.last
  end

  def submit_answer
    @multiple_choice_question = MultipleChoiceQuestion.find(params[:id])
    selected_choice = Choice.find(params[:selected_choice])
    @user = current_user
    #Buscamos el task para actualizar el json/diccionario
    @task = @user.tasks.last
    # Check if the answer is correct
    is_correct = selected_choice.correct?


    # Add the question ID to the answered list
    @task.answered << @multiple_choice_question.id
    @task.answered.uniq!

    if !is_correct
      # If the answer is incorrect, add the question ID to the wrongs list
      @task.wrongs << @multiple_choice_question.id
      @task.wrongsaux << @multiple_choice_question.id
      @task.wrongs.uniq!
      @task.wrongsaux.uniq!


    else
      @task.score += 1
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

      redirect_to results_path(task_id: @task.id)
    end
  end

  def redo_answer
    @multiple_choice_question = MultipleChoiceQuestion.find(params[:id])
    selected_choice = Choice.find(params[:selected_choice])
    @user = current_user
    #Buscamos el task para actualizar el json/diccionario
    @task = @user.tasks.last
    @task.redo = true
    # Check if the answer is correct
    is_correct = selected_choice.correct?

    #Marcamos como respondida la pregunta
    @task.answered << @multiple_choice_question.id
    @task.answered.uniq!

    next_question = @task.multiple_choice_questions
    .where.not(id: @task.answered).where(id: @task.wrongs)
    .sample

    puts '---------------------------'
    puts @task.wrongs
    puts @task.answered
    puts '---------------------------'

    if is_correct
      @task.wrongs.delete(@multiple_choice_question.id)
      @task.score += 1
    end

    @task.save
    if next_question
      redirect_to multiple_choice_question_path(next_question)
    else
      # Handle the case where there are no more questions
      redirect_to results_path(task_id: @task.id)
    end
  end
end
