class CommentsController < ApplicationController
  def create
    @ticket = Ticket.find(params[:ticket_id])
    @comment = @ticket.comments.build(comment_params)
    @comment.user = current_user

    if @comment.save
      flash[:notice] = "Comment added successfully!"
      redirect_to @ticket
    else
      flash[:alert] = "Comment cannot be blank"
      redirect_to @ticket
    end
  end

  private

  def comment_params
    params.require(:comment).permit(:body)
  end
end
