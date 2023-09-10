class RemoveImageFromTickets < ActiveRecord::Migration[7.0]
  def change
    remove_column :tickets, :image, :string
  end
end
