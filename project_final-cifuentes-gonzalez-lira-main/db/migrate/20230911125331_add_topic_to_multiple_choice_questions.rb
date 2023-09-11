class AddTopicToMultipleChoiceQuestions < ActiveRecord::Migration[7.0]
  def change
    add_column :multiple_choice_questions, :topic, :text
  end
end
