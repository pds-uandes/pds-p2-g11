from django.shortcuts import render, redirect
from .models import *
import random
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login

class UserLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_student = True
        user.save()

        valid = super().form_valid(form)  # Call super().form_valid(form) first

        # Authenticate the user
        authenticated_user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],  # Assuming you're using Django's UserCreationForm or similar
        )

        # Log in the user
        login(self.request, authenticated_user)

        return valid  # Return the result of super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')




from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    #borrar la task actual
    if 'task_id' in request.session:
        del request.session['task_id']

    context = {'tasks': Task.objects.all()}

    if request.GET.get('task'):
        # delete the task_id from the session
        return redirect(f"quiz/?task={request.GET.get('task')}")

    return render(request, 'home.html', context)

def quiz(request):
    task_uid = request.GET.get('task')
    if task_uid:
        try:
            task = Task.objects.get(uid=task_uid)
            context = {'task': task}
            return render(request, 'quiz.html', context)
        except Task.DoesNotExist:
            pass

    # Handle the case when the task doesn't exist or task_uid is not provided.
    return HttpResponse("Task not found or invalid request!")

def get_quiz(request):
    try:
        task_uid = request.GET.get('task')
        if task_uid:
            task = Task.objects.get(uid=task_uid)
            question_objs = Question.objects.filter(task=task)
        else:
            question_objs = Question.objects.all()

        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                "uid": question_obj.uid,
                "task": task.uid if task else None,
                "question": question_obj.question_text,
                "difficulty": question_obj.get_difficulty_display(),
                "answers": question_obj.get_answers()
            })
        payload = {'status': True, 'data': data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong!")

def do_task(request):
    json_user = request.user.json_user

    if 'task_id' not in request.session:
        # If not, create a new task
        task = Task()
        task.questions.clear()
        task.save()
        task_id = str(task.uid)
        request.session['task_id'] = task_id
    else:
        # If there is an active task, fetch the task and question number
        task_id = request.session['task_id']
        task_id = uuid.UUID(task_id)  # Convert the stored string back to a UUID
        task = Task.objects.get(pk=task_id)
        task.counter += 1

        if request.method == "POST":
            question_text = request.POST.get('question')
            question = Question.objects.get(question_text=question_text)
            selected_answer = request.POST.get('selected_answer')

            # Get the correct answer from the question's answers
            correct_answer = None

            for answer in question.get_answers():
                if answer['is_correct']:
                    correct_answer = answer['answer']
                    break

            print(f"Correct answer: {correct_answer}")
            print(f"Selected answer: {selected_answer}")

            # Compare the selected answer with the correct answer
            if selected_answer == correct_answer:
                print("The selected answer is CORRECT.")
                task.score += 1
                
            else:
                print("The selected answer is INCORRECT.")


        task.save()

    # get the questions
    question = task.add_question(json_user['level'], json_user['type_task'], json_user['difficulty'])
    task.questions.append(question[0])
    task.save()

    if task.counter >= 5:
        return render(request, 'results.html', {'questions': task.questions, 'score': task.score})

    return render(request, 'new_quiz.html', {'question': task.questions[-1], 'counter': task.counter + 1})


# Create a view for the results page


def results(request):
    # Retrieve the task and its score here to display on the results page
    task_id = request.session.get('task_id')
    if task_id:
        task = Task.objects.get(pk=task_id)
        score = task.score
    else:
        score = None

    return render(request, 'results.html', {'score': score})
