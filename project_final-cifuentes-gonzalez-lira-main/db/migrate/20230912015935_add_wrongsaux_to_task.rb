class AddWrongsauxToTask < ActiveRecord::Migration[7.0]
  def change
    add_column :tasks, :wrongsaux, :jsonb, default: []
  end
end
