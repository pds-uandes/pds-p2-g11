class Parameter < ApplicationRecord
    belongs_to :numeric_question

    validates :name, presence: true
    validates :min_value, :max_value, numericality: { only_integer: true }
  end
