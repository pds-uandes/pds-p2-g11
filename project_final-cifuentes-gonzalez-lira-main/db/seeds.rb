# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: "Star Wars" }, { name: "Lord of the Rings" }])
#   Character.create(name: "Luke", movie: movies.first)



require 'faker'

# Delete all previous instances of models created
ActiveStorage::Attachment.delete_all
ActiveStorage::Blob.delete_all
ActiveStorage::VariantRecord.delete_all
Comment.delete_all
Tag.delete_all
Ticket.delete_all
User.delete_all

# Create 2 admins, 2 supervisors, 2 executives and 10 normal users
2.times do
  User.create!(
    email: Faker::Internet.email,
    password: '123456',
    first_name: Faker::Name.first_name,
    last_name: Faker::Name.last_name,
    role: :admin
  )
end

2.times do
  User.create!(
    email: Faker::Internet.email,
    password: '123456',
    first_name: Faker::Name.first_name,
    last_name: Faker::Name.last_name,
    role: :supervisor
  )
end

2.times do
  User.create!(
    email: Faker::Internet.email,
    password: '123456',
    first_name: Faker::Name.first_name,
    last_name: Faker::Name.last_name,
    role: :executive
  )
end

10.times do
  User.create!(
    email: Faker::Internet.email,
    password: '123456',
    first_name: Faker::Name.first_name,
    last_name: Faker::Name.last_name,
    role: :normal
  )
end

# Create 20 tickets and tags and comments as well
70.times do |i|
  ticket = Ticket.create!(
    normal_user_id: User.normal.sample.id,
    executive_user_id: User.executive.sample.id,
    title: "Ticket #{i}",
    description: Faker::Lorem.paragraph(sentence_count: 5),
    state: Ticket.states.values.sample,
    priority: :low,
    deadline: Faker::Time.forward(days: rand(1..30)),
    incident_date: Faker::Time.backward(days: rand(1..30)),
    closed_at: Faker::Time.backward(days: rand(1..30))
  
  )

  rand(1..5).times do
    Comment.create!(
      body: Faker::Lorem.paragraph(sentence_count: 3),
      ticket_id: ticket.id,
      user_id:
        if [true, false].sample
          ticket.normal_user_id
        else
          ticket.executive_user_id
        end
    )
  end

  rand(1..5).times do
    tag = Tag.find_or_create_by!(name: "Tag #{rand(1..10)}")
    ticket.tags << tag unless ticket.tags.include?(tag)
  end
end

puts "Created #{User.count} users"
puts "Created #{Ticket.count} tickets"
puts "Created #{Comment.count} comments"
puts "Created #{Tag.count} tags"


User.create!(
  email: 'a1@gmail.com',
  password: 'asdfasdf',
  first_name: 'a1',
  last_name: 'a1',
  role: :admin # or any other role you want to assign
)
User.create!(
  email: 's1@gmail.com',
  password: 'asdfasdf',
  first_name: 's1',
  last_name: 's1',
  role: :supervisor # or any other role you want to assign
)
User.create!(
  email: 'e1@gmail.com',
  password: 'asdfasdf',
  first_name: 'e1',
  last_name: 'e1',
  role: :executive # or any other role you want to assign
)
User.create!(
  email: 'e2@gmail.com',
  password: 'asdfasdf',
  first_name: 'e2',
  last_name: 'e2',
  role: :executive # or any other role you want to assign
)
User.create!(
  email: 'n1@gmail.com',
  password: 'asdfasdf',
  first_name: 'n1',
  last_name: 'n1',
  role: :normal # or any other role you want to assign
)
User.create!(
  email: 'n2@gmail.com',
  password: 'asdfasdf',
  first_name: 'n2',
  last_name: 'n2',
  role: :normal # or any other role you want to assign
)
