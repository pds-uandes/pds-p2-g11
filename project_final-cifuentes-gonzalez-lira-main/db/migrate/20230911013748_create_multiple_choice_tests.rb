class CreateMultipleChoiceTests < ActiveRecord::Migration[7.0]
  def change
    create_table :multiple_choice_tests do |t|
      t.integer :score

      t.timestamps
    end
  end
end
