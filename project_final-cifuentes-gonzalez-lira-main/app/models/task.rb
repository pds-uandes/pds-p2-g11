class Task < ApplicationRecord
    belongs_to :user, optional: true
    has_and_belongs_to_many :multiple_choice_questions, join_table: :task_mcq_joint
    has_and_belongs_to_many :numeric_questions, join_table: :tasks_numeric_questions
end
