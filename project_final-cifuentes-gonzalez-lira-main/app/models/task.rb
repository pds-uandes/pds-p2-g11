class Task < ApplicationRecord
    belongs_to :user, optional: true
    has_and_belongs_to_many :multiple_choice_questions, join_table: :task_mcq_joint
end
