class AddTestAndQuestionToUsers < ActiveRecord::Migration[7.0]
  def change
    add_column :users, :test, :integer, limit: 1
    add_column :users, :question, :integer
  end
end
