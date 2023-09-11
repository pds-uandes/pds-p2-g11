class AddAnswerToNumericQuestion < ActiveRecord::Migration[7.0]
  def change
    add_column :numeric_questions, :answer, :float
  end
end
