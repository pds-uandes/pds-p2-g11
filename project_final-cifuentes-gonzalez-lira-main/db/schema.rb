# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.0].define(version: 2023_09_11_223548) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "choices", force: :cascade do |t|
    t.text "answer"
    t.boolean "correct"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "multiple_choice_question_id", null: false
    t.index ["multiple_choice_question_id"], name: "index_choices_on_multiple_choice_question_id"
  end

  create_table "multiple_choice_questions", force: :cascade do |t|
    t.text "question"
    t.integer "difficulty"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.text "hint"
    t.text "topic"
    t.bigint "task_id"
    t.index ["task_id"], name: "index_multiple_choice_questions_on_task_id"
  end

  create_table "numeric_answers", force: :cascade do |t|
    t.text "respuesta"
    t.boolean "correct"
    t.text "equation"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "numeric_question_id"
    t.text "hint"
    t.index ["numeric_question_id"], name: "index_numeric_answers_on_numeric_question_id"
  end

  create_table "numeric_questions", force: :cascade do |t|
    t.text "pregunta"
    t.integer "difficulty"
    t.integer "score"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "topic"
    t.binary "image_data"
  end

  create_table "parameters", force: :cascade do |t|
    t.integer "number"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "numeric_question_id"
    t.index ["numeric_question_id"], name: "index_parameters_on_numeric_question_id"
  end

  create_table "task_mcq_joint", id: false, force: :cascade do |t|
    t.bigint "task_id"
    t.bigint "multiple_choice_question_id"
    t.index ["multiple_choice_question_id"], name: "index_task_mcq_joint_on_multiple_choice_question_id"
    t.index ["task_id"], name: "index_task_mcq_joint_on_task_id"
  end

  create_table "tasks", force: :cascade do |t|
    t.integer "score"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "topic"
    t.jsonb "questions"
    t.bigint "user_id"
    t.jsonb "answered", default: []
    t.jsonb "wrongs", default: []
    t.boolean "redo", default: false
    t.index ["user_id"], name: "index_tasks_on_user_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "first_name", default: "", null: false
    t.string "last_name", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "role"
    t.integer "task"
    t.integer "question"
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

  add_foreign_key "choices", "multiple_choice_questions"
  add_foreign_key "multiple_choice_questions", "tasks"
  add_foreign_key "numeric_answers", "numeric_questions"
  add_foreign_key "parameters", "numeric_questions"
  add_foreign_key "task_mcq_joint", "multiple_choice_questions"
  add_foreign_key "task_mcq_joint", "tasks"
  add_foreign_key "tasks", "users"
end
