# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: "Star Wars" }, { name: "Lord of the Rings" }])
#   Character.create(name: "Luke", movie: movies.first)



# require 'faker'
mcq = MultipleChoiceQuestion.create!(question: "What is the capital of France?", difficulty: 1)
choice = Choice.create!(answer: "Paris", correct: true, multiple_choice_question: mcq)


