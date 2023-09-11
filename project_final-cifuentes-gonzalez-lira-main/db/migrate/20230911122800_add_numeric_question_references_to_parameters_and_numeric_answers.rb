class AddNumericQuestionReferencesToParametersAndNumericAnswers < ActiveRecord::Migration[7.0]
  def change
    add_reference :parameters, :numeric_question, foreign_key: true
    add_reference :numeric_answers, :numeric_question, foreign_key: true
  end
end
