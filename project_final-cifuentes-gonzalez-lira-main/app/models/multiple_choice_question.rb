class MultipleChoiceQuestion < ApplicationRecord
  has_many :choices, dependent: :destroy
end
