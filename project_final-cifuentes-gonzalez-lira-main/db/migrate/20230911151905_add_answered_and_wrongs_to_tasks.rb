class AddAnsweredAndWrongsToTasks < ActiveRecord::Migration[7.0]
  def change
    add_column :tasks, :answered, :jsonb, default: []
    add_column :tasks, :wrongs, :jsonb, default: []
  end
end
