class AddDetailsToTickets < ActiveRecord::Migration[7.0]
  def change
    add_column :tickets, :title, :string
    add_column :tickets, :description, :text
    add_column :tickets, :state, :integer
    add_column :tickets, :priority, :integer
    add_column :tickets, :deadline, :datetime
  end
end
