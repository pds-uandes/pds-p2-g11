<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
=======
from django.shortcuts import get_object_or_404, render, redirect


# # Create your views here.
from django.http import HttpResponse
from .models import Question
from django.contrib.auth import authenticate, login
from django.contrib import messages
>>>>>>> login

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


def vote(request, question_id):
<<<<<<< HEAD
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message.
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",
        })
    
    # Check if the selected choice is correct
    if selected_choice.is_correct:
        result_message = "Your answer is correct!"
    else:
        result_message = "Sorry, your answer is incorrect."

    # Increment the vote count for the selected choice

    
    # Redirect to the results page with a result message
    return render(request, "polls/results.html", {
        "question": question,
        "result_message": result_message,
    })

=======
    return HttpResponse("You're voting on question %s." % question_id)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
>>>>>>> login
