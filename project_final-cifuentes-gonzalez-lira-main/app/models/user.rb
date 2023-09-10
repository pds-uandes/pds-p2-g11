class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable


  before_create :set_default_role


  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  validates :first_name, presence: true
  validates :last_name, presence: true



  enum role: { normal: 0, executive: 1, supervisor: 2, admin: 3 }

  belongs_to :supervisor, class_name: 'User', optional: true
  has_many :executives, class_name: 'User', foreign_key: 'supervisor_id'
  has_many :supervisors, class_name: 'User', foreign_key: 'admin_id'
  belongs_to :admin, class_name: 'User', optional: true
  has_many :comments

  #Tickets
  has_many :normal_user_tickets, class_name: 'Ticket', foreign_key: 'normal_user_id', dependent: :destroy
  has_many :executive_user_tickets, class_name: 'Ticket', foreign_key: 'executive_user_id'

  def full_name
    "#{first_name } #{last_name}"
  end
  
  private

  def set_default_role
    self.role ||= :normal
  end

  
end
