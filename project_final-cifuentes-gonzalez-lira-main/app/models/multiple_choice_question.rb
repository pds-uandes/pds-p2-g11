class MultipleChoiceQuestion < ApplicationRecord
  has_many :choices, dependent: :destroy
  belongs_to :task, optional: true
  has_and_belongs_to_many :tasks, join_table: :task_mcq_joint
end
