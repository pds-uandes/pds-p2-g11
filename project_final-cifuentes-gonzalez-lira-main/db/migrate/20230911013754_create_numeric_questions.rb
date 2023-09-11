class CreateNumericQuestions < ActiveRecord::Migration[7.0]
  def change
    create_table :numeric_questions do |t|
      t.text :pregunta
      t.integer :difficulty
      t.integer :score

      t.timestamps
    end
  end
end
