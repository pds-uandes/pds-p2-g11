class NumericQuestion < ApplicationRecord
  has_many :numeric_answers, dependent: :destroy
  has_many :numeric_tests, through: :numeric_answers
  has_one_attached :image
end
