Rails.application.routes.draw do
  devise_for :users
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
  root "static_pages#home"

  resources :users do
    post 'start_task', on: :member
  end


  resources :numeric_questions, only: [:show] do
    post 'submit_answer', on: :member
    post 'redo_answer', on: :member
  end

  resources :multiple_choice_questions, only: [:show] do
    post 'submit_answer', on: :member
    get 'redo_answer', on: :collection, to: 'multiple_choice_questions#redo_answer'
    post 'redo_answer', on: :member
  end

  resources :results, only: [:index]
end
