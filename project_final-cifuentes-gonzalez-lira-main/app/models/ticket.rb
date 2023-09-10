class Ticket < ApplicationRecord
    has_many :comments, dependent: :destroy
    has_and_belongs_to_many :tags
    before_create :set_default_state
    after_create :set_deadline

    has_many_attached :images , dependent: :destroy

  
    belongs_to :normal_user, class_name: 'User'
    belongs_to :executive_user, class_name: 'User'
  
    validates :title, presence: true
    validates :description, presence: true
  
    validates :state, presence: true, inclusion: { in: %w[open closed reopened] }
    validates :priority, presence: true, inclusion: { in: %w[urgent high medium low] }
    validates :deadline, presence: true
  
    validates :response_quality, numericality: { only_integer: true, greater_than_or_equal_to: 1, less_than_or_equal_to: 5 }, allow_nil: true
  
    enum state: { open: 0, closed: 1, reopened: 2 }
    
    after_initialize do |ticket|
      ticket.incident_date ||= Time.current
      ticket.priority ||= 'low'
      ticket.state ||= 'open'
    end
  
    def creation_date
      created_at.strftime("%e %b %Y")
    end
    
    def formatted_deadline
      deadline.strftime("%e %b %Y")
    end

  
    def self.search(search)
      if search
        joins(:normal_user).where('title LIKE :search OR description LIKE :search OR users.email LIKE :search', search: "%#{search}%")
      else
        all
      end
    end
  

    scope :order_by_priority, ->(order = :asc) {
      order = order.to_sym
      order_query = "CASE priority WHEN 'urgent' THEN 1 WHEN 'high' THEN 2 WHEN 'medium' THEN 3 WHEN 'low' THEN 4 END"
      order(Arel.sql(order_query) => order)
    }

    private
    
    def set_default_state
      self.state = :open if state.nil?
    end
    
    def set_deadline
      self.deadline = self.created_at + 1.month
      self.save
    end

    
  end
  