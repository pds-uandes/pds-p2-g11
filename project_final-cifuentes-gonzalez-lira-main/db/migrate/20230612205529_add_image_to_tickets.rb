class AddImageToTickets < ActiveRecord::Migration[7.0]
  def change
    add_column :tickets, :image, :string
  end
end
