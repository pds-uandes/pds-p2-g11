class NumericAnswer < ApplicationRecord
  belongs_to :numeric_question

  def calculate_answer
    eval(answer.gsub(/(\w+)/) { |m| numeric_question.parameters.find_by(name: m)&.value.to_s })
  end
end
