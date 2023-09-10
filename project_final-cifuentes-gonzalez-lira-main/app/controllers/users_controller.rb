class UsersController < ApplicationController
    def show
        @user = User.find(params[:id])
    end
    
  before_action :authenticate_user!
  before_action :ensure_authorized_user, only: [:index]

  def index
    @normal_users = User.normal
    @executive_users = User.executive
    @supervisor_users = User.supervisor
    @admin_users = User.admin
  end
    
    def edit
        @user = User.find(params[:id])
    end

    def update
        @user = User.find(params[:id])
        if @user.update(user_params)
          redirect_to @user, notice: "User was successfully updated."
        else
          render :edit
        end
      end
    
    def user_params
      params.require(:user).permit(:role)
    end
  private
  def ensure_authorized_user
    unless current_user.admin? || current_user.supervisor?
      redirect_to root_path, alert: 'You are not authorized to access this page'
    end
  end

end
