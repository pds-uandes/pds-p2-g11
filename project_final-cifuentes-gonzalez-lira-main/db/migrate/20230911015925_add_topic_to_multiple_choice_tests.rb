class AddTopicToMultipleChoiceTests < ActiveRecord::Migration[7.0]
  def change
    add_column :multiple_choice_tests, :topic, :string
  end
end
