class AddDefaultTaskValueToUsers < ActiveRecord::Migration[7.0]
  def change
    change_column_default :users, :task, 0
  end
end
