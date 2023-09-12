class JointTaskMcqTable < ActiveRecord::Migration[7.0]
  def change
    create_table :task_mcq_joint, id: false do |t|
      t.references :task, foreign_key: true
      t.references :multiple_choice_question, foreign_key: true
    end
  end
end
