from django.shortcuts import render, redirect
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
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseForbidden

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

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    context = {'tasks': Task.objects.all()}

    if request.GET.get('task'):
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
