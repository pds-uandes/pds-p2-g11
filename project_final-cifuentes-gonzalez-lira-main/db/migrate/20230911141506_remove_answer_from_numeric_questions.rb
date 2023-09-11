class RemoveAnswerFromNumericQuestions < ActiveRecord::Migration[7.0]
  def change
    remove_column :numeric_questions, :answer, :float
  end
end
