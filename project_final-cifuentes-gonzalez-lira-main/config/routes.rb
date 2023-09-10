Rails.application.routes.draw do
  devise_for :users
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
  root "static_pages#home"
  
  resources :users

  resources :tickets do
    get :reports, on: :collection
    member do
      patch :accept_response
      patch :reopen
      post :add_tag
    end
    resources :comments, only: [:create]
  end
  get '/tickets/search', to: 'tickets#search'
  get 'overdue_ticket_report', to: 'tickets#overdue_ticket_report'
  get 'executive_performance_report', to: 'tickets#executive_performance_report', as: :executive_performance_report


end
