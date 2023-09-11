class AddTaskToMultipleChoiceQuestions < ActiveRecord::Migration[7.0]
  def change
    add_reference :multiple_choice_questions, :task, null: true, foreign_key: true

    # Assuming all questions belong to the first task
    first_task = Task.first
    MultipleChoiceQuestion.update_all(task_id: first_task.id)

    change_column_null :multiple_choice_questions, :task_id, false
  end
end
