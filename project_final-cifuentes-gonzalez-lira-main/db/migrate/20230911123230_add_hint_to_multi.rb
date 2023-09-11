class AddHintToMulti < ActiveRecord::Migration[7.0]
  def change
    add_column :multiple_choice_questions, :hint, :text
    add_column :numeric_answers, :hint, :text
  end
end
