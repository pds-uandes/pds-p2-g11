from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import random
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponseForbidden
from django.contrib.auth.views import LoginView, LogoutView
from django.utils import timezone
from django.contrib.auth.views import LogoutView
from django.utils import timezone

class CustomLoginView(LoginView):
    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Update the last logout time and calculate session duration
        if request.user.is_authenticated:
            request.user.last_logout_time = timezone.now()
            if request.user.last_login_time is not None:
                session_duration = request.user.last_logout_time - request.user.last_login_time
                request.user.total_time_spent += session_duration
            request.user.save()

        return super().dispatch(request, *args, **kwargs)



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


@method_decorator(login_required, name='dispatch')
class StudentListView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return HttpResponseForbidden("You are not allowed to view this page.")
        students = CustomUser.objects.filter(is_student=True)
        return render(request, 'students.html', {'students': students})



@login_required(login_url='/login/')
def home(request):
    tasks = Task.objects.all()
    students = CustomUser.objects.filter(is_student=True)
    if request.GET.get('task'):
        return redirect(f"quiz/?task={request.GET.get('task')}")
    
    context = {'tasks': tasks, 'students': students}
    return render(request, 'home.html', context)

def student_profile(request, student_id):
    student = get_object_or_404(CustomUser, pk=student_id)
    if student.last_login_time and student.last_logout_time:
        usage_time = student.last_logout_time - student.last_login_time
    else:
        usage_time = "Not available"
    return render(request, 'student_profile.html', {'student': student, 'usage_time': usage_time})

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
    # Check if there is an active task in the session
    json_user = {
    'difficulty': 1,
    'level': 0,
    'type_task': 0,
    }

    if 'task_id' not in request.session:
        # If not, create a new task
        task = Task()

        questions = task.add_questions(json_user['level'], json_user['type_task'], json_user['difficulty'])

        task.save()
        task_id = str(task.uid)
        request.session['task_id'] = task_id
    else:
        # If there is an active task, fetch the task and question number
        task_id = request.session['task_id']
        task_id = uuid.UUID(task_id)  # Convert the stored string back to a UUID
        task = Task.objects.get(pk=task_id)
        task.counter += 1
        task.save()

    print(questions)
    if task.counter >= 5:
        return render(request, 'results.html', {'questions': questions})

    return render(request, 'new_quiz.html', {'questions': questions[task.counter]})

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
