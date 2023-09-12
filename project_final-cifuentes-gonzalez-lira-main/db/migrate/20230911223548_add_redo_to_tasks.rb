class AddRedoToTasks < ActiveRecord::Migration[7.0]
  def change
    add_column :tasks, :redo, :boolean, default: false
  end
end
