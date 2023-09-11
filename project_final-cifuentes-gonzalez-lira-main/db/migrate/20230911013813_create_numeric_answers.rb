class CreateNumericAnswers < ActiveRecord::Migration[7.0]
  def change
    create_table :numeric_answers do |t|
      t.text :respuesta
      t.boolean :correct
      t.text :equation

      t.timestamps
    end
  end
end
