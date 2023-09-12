class ChangeColumnNameAndLimitInUsers < ActiveRecord::Migration[7.0]
  def change
    change_table :users do |t|
      t.rename :test, :task # Change column name from "test" to "task"
      t.change :task, :integer, limit: 4 # Set the limit to 4
    end
  end
end
