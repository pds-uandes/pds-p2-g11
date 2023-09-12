Rails.application.routes.draw do
  devise_for :users
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
  root "static_pages#home"

  resources :users do
    post 'start_task', on: :member
  end

  resources :multiple_choice_questions do
    post 'submit_answer', on: :member
    post 'redo_answer', on: :member  # Add this line
  end

  resources :multiple_choice_questions, only: [:show]  # Add this line
  resources :results, only: [:index]

  post 'multiple_choice_questions/:id/redo_answer', to: 'multiple_choice_questions#redo_answer', as: :redo_answer_multiple_choice_question
end
