class CreateChoices < ActiveRecord::Migration[7.0]
  def change
    create_table :choices do |t|
      t.text :answer
      t.boolean :correct

      t.timestamps
    end
  end
end
