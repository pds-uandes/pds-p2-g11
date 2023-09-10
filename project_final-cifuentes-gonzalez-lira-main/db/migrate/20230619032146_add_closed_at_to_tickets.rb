class AddClosedAtToTickets < ActiveRecord::Migration[7.0]
  def change
    add_column :tickets, :closed_at, :datetime
  end
end
