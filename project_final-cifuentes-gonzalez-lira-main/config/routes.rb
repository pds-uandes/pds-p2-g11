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
  end
  resources :multiple_choice_questions, only: [:show]  # Add this line



end
