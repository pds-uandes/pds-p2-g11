class CreateMultipleChoiceQuestions < ActiveRecord::Migration[7.0]
  def change
    create_table :multiple_choice_questions do |t|
      t.text :question
      t.integer :difficulty

      t.timestamps
    end
  end
end
