class RenameMultipleChoiceTestsToTasks < ActiveRecord::Migration[7.0]
  def change
    rename_table :multiple_choice_tests, :tasks
  end
end
