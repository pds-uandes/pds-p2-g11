class Task < ApplicationRecord
    belongs_to :user
    has_many :multiple_choice_questions

end
