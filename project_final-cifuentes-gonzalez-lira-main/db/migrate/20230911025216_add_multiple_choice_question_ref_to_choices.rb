class AddMultipleChoiceQuestionRefToChoices < ActiveRecord::Migration[7.0]
  def change
    add_reference :choices, :multiple_choice_question, null: false, foreign_key: true
  end
end
