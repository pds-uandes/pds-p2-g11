# db/migrate/xxxxxx_create_tasks_numeric_questions_join_table.rb
class CreateTasksNumericJoinTable < ActiveRecord::Migration[7.0]
  def change
    create_table :tasks_numeric_questions, id: false do |t|
      t.references :task, foreign_key: true
      t.references :numeric_question, foreign_key: true
    end
  end
end
