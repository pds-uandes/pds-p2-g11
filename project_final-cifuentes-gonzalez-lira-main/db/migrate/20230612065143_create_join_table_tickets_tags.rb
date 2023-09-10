class CreateJoinTableTicketsTags < ActiveRecord::Migration[7.0]
  def change
    create_join_table :tickets, :tags do |t|
      # t.index [:ticket_id, :tag_id]
      # t.index [:tag_id, :ticket_id]
    end
  end
end
