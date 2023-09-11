class AddImageToNumericQuestions < ActiveRecord::Migration[7.0]
  def change
    add_column :numeric_questions, :image_data, :binary
  end
end
