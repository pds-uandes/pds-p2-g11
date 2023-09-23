from django.shortcuts import render, redirect
from .models import *
import random
import uuid
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

# crear un task
# agregarle 5 preguntas de base de datos a ese task recien creado

# def do_task(request):
#     # este json tiene que estar en el modelo usuario una vez creado
#     json_user = {
#         'difficulty': 1,
#         'level': 0,
#         'type_task': 0,
#     }

#     task = Task()
#     task.save()
#     questions =task.add_questions(json_user['level'], json_user['type_task'], json_user['difficulty'])
#     context = {'questions': questions[task.counter], 'counter': task.counter}
#     print("PRINTE DE QUESTIONS")
#     q = list(questions)
#     print(q[0].question_text)
#     print("PRINTE DE QUESTIONS")
#     if task.counter < 5:
#         return render(request, 'new_quiz.html', context)
#     else:
#         return render(request, 'results.html', {'score': task.score})

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
        task.save()
        task_id = str(task.uid)
        request.session['task_id'] = task_id
        request.session['question_number'] = 0
    else:
        # If there is an active task, fetch the task and question number
        task_id = request.session['task_id']
        task_id = uuid.UUID(task_id)  # Convert the stored string back to a UUID
        task = Task.objects.get(pk=task_id)
        task.counter += 1
        task.save()

    question_number = request.session.get('question_number', 0)  # Get question_number if it exists, otherwise default to 0

    # Check if the task has reached 5 questions, if so, redirect to results page
    if task.counter >= 5:
        return render(request, 'results.html', {'questions': question_number})

    # Fetch a new question for the current task and question number
    questions = task.add_questions(json_user['level'], json_user['type_task'], json_user['difficulty'])

    # Update the session variable with the incremented question number
    request.session['question_number'] = question_number + 1

    return render(request, 'new_quiz.html', {'questions': questions[0]})

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

