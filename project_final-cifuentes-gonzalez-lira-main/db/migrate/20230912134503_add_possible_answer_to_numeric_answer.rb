class AddPossibleAnswerToNumericAnswer < ActiveRecord::Migration[7.0]
  def change
    add_column :numeric_answers, :possible_answer, :text
  end
end
