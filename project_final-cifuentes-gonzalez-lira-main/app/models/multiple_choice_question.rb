class MultipleChoiceQuestion < ApplicationRecord
  has_many :choices, dependent: :destroy
  belongs_to :task
end
