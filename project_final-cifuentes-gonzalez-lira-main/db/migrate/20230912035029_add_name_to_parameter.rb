class AddNameToParameter < ActiveRecord::Migration[7.0]
  def change
    add_column :parameters, :name, :string
  end
end
