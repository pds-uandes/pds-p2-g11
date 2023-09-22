from django.shortcuts import render, redirect
from .models import *
import random
from django.http import JsonResponse, HttpResponse

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
