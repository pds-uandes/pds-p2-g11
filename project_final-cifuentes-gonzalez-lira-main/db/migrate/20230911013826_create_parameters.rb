class CreateParameters < ActiveRecord::Migration[7.0]
  def change
    create_table :parameters do |t|
      t.integer :number
      t.timestamps
    end
  end
end
