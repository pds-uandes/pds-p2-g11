class ChangeMultipleChoiceQuestions < ActiveRecord::Migration[7.0]
  def change
    change_column_null :multiple_choice_questions, :task_id, true
  end
end
