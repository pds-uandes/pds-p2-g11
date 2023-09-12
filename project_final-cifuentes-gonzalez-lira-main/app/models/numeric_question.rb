class NumericQuestion < ApplicationRecord
  has_many :numeric_answers, dependent: :destroy
  has_many :numeric_tests, through: :numeric_answers
  has_many :parameters
  has_one_attached :image
  has_and_belongs_to_many :tasks, join_table: :tasks_numeric_questions

  def generate_parameter_values
    parameters.each do |parameter|
      parameter.value = rand(parameter.min_value..parameter.max_value)
      parameter.save
    end
  end

  def question_with_values
    # question.gsub(/_/) { parameters.shift.value }
  end
end
