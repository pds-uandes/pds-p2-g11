class AddFieldsToTickets < ActiveRecord::Migration[6.1]
  def change
    add_column :tickets, :incident_date, :datetime
    add_column :tickets, :executive_response, :text
    add_column :tickets, :response_quality, :integer

    change_column :tickets, :state, :integer, using: 'state::integer'
    change_column_default :tickets, :state, from: nil, to: 0

    change_column :tickets, :priority, :string
    change_column_default :tickets, :priority, from: nil, to: 'low'
  end
end
