class Ability
  include CanCan::Ability

  def initialize(user)
    if user.present?
      # Abilities for logged in users
      if user.normal? || user.executive?
        cannot :manage, User
      end

      if user.admin? || user.supervisor?
        can :read, :reports
        can :read, :overdue_ticket_report
        can :read, :executive_performance_report
      else
        cannot :read, :reports
        cannot :read, :overdue_ticket_report
        cannot :read, :executive_performance_report
      end
    else
      # Abilities for users who are not logged in
      cannot :manage, :all
      can :read, :all
    end
  end
end
