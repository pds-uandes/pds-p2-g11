class DropModelNameTable < ActiveRecord::Migration[7.0]
  def up
    drop_table :active_storage_attachments, force: :cascade
    drop_table :active_storage_blobs, force: :cascade
    drop_table :active_storage_variant_records, force: :cascade
    drop_table :comments, force: :cascade
    drop_table :tags, force: :cascade
    drop_table :tags_tickets, force: :cascade
    drop_table :tickets, force: :cascade
  end

  def down
    raise ActiveRecord::IrreversibleMigration
  end
end
