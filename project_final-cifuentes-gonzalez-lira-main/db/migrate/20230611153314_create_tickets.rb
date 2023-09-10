class CreateTickets < ActiveRecord::Migration[7.0]
  def change
    create_table :tickets do |t|
      t.references :normal_user, foreign_key: { to_table: :users }
      t.references :executive_user, foreign_key: { to_table: :users }

      t.timestamps
    end
  end
end
