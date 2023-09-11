class AddTopicToNumericQuestions < ActiveRecord::Migration[7.0]
  def change
    add_column :numeric_questions, :topic, :string
  end
end
