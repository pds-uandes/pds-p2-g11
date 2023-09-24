from django.db import models
import uuid
# Create your models here.
import sympy
import random
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    total_time_spent = models.DurationField(default=timedelta())

    json_user = {
    'difficulty': 1,
    'level': 0,
    'type_task': 0,
    }


class Task(BaseModel):
    tries = {
        'first_try_answered': False,
        'second_try': False,
        'second_try_answered': False,
        'user_answered': False,
    }
    wrongs = []
    wrongs_permanent = []
    questions = []
    counter = models.IntegerField(default=0)
    wrongs_counter = models.IntegerField(default=-1)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Task - {self.uid}"

    def update_score(self, score):
        self.score = score
        self.save()

    def update_trys(self, parameter):
        self.trys[parameter] = True
        self.save()

    def add_question(self, level, task_type, difficulty):
        if level == 0:
            theme = 1

        question_query = Q(difficulty=difficulty) & Q(theme=theme)
        # type 0: multiple choice questions
        # type 1: numeric question
        if task_type == 0:
            question = Question.objects.filter(question_query).order_by('?')[0]
            return question

# ===================== MCQ =====================
class Question(BaseModel):
    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Hard')]

    THEME_CHOICES = [
        (1, 'Caracteristicas de la onda'),
        (2, 'Ondas Sonoras'),
        (3, 'Ondas Armonicas'),
        (4, 'Ecuacion de la Onda'),
        (5, 'Energias e info. transferida')]

    task = models.ForeignKey(Task, related_name='task_questions', on_delete=models.CASCADE, null=True, blank=True)
    question_text = models.CharField(max_length=100)
    hint = models.CharField(max_length=100, null=True, blank=True)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)
    theme = models.IntegerField(choices=THEME_CHOICES, default=1)

    def __str__(self) -> str:
        return self.question_text

    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question = self))
        random.shuffle(answer_objs)
        data = []
        for answer_obj in answer_objs:
            data.append({
                "answer": answer_obj.answer,
                "is_correct": answer_obj.is_correct
            })
        return data


class Answer(BaseModel):
    question = models.ForeignKey(Question,related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer

# ===================== NUMERIC =====================
class DinamicQuestion(BaseModel):
    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Hard')]

    THEME_CHOICES = [
        (1, 'Caracteristicas de la onda'),
        (2, 'Ondas Sonoras'),
        (3, 'Ondas Armonicas'),
        (4, 'Ecuacion de la Onda'),
        (5, 'Energias e info. transferida')]

    task = models.ForeignKey(Task, related_name='dinamic_task_questions', on_delete=models.CASCADE, null=True, blank=True)

    question_text = models.CharField(max_length=1000)
    hint = models.CharField(max_length=100, null=True, blank=True)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)
    theme = models.IntegerField(choices=THEME_CHOICES, default=1)

    # Encuentra la distancia entre dos puntos si recorre a una velocidad de [VELOCIDAD] m/s durante [TIEMPO] segundos [DISTANCIA] [CACHE]

    def __str__(self) -> str:
        return self.question_text

    def replace_parameters(self):
        parameters_objs = list(Parameters.objects.filter(question = self))
        self.parameters = parameters_objs
        for parameter in parameters_objs:
            self.question_text = self.question_text.replace(parameter.parameter, str(parameter.value))

    def fill_answers(self):
        answer_objs = list(Answer.objects.filter(question = self))
        for answer in answer_objs:
            for parameter in self.parameters:
                answer.dic[parameter.parameter] = parameter.value
            answer.equation_value()
            answer.save()

    def get_answers(self):
        #Ir al string de la pregunta y buscar donde reemplazar con la funcion
        #Entregar el string finalizado

        answer_objs = list(Answer.objects.filter(question = self))
        data = []
        for answer_obj in answer_objs:
            answer_obj.equation_value()
            print(answer_obj.parameters)
            data.append({
                'equation': answer_obj.equation,
                'metrics': answer_obj.metrics,
                'result': answer_obj.result,
            })
        return data

class DinamicAnswer(BaseModel):
    question = models.ForeignKey(Question,related_name='dinamic_question_answer', on_delete=models.CASCADE)

    dic = {"[VELOCIDAD]": 0,
            "[TIEMPO]": 0,
            "[DISTANCIA]": 0,
            '[FRECUENCIA]': 0,
            '[LONGITUD]': 0,
            '[PERIODO]': 0,
            '[AMPLITUD]': 0}

    metrics = models.CharField(max_length=100)
    equation = models.CharField(max_length=1000, blank=True)

    def __str__(self) -> str:
        return self.answer

    def equation_value(self):
        # Parse the equation
        expr = sympy.sympify(self.equation)

        result = expr.subs(self.dic)

        self.result = [round(result.evalf(), 3) - round(result.evalf(), 3)*0.05, round(result.evalf(), 3) + round(result.evalf(), 3)*0.05]

class Parameters(BaseModel):
    question = models.ForeignKey(Question,related_name='dinamic_question_parameters', on_delete=models.CASCADE)
    parameter = models.CharField(max_length=100)
    min_val = models.IntegerField(default=0)
    max_val = models.IntegerField(default=0)

    def generate_random_value(self):
        min_value = self.min_val
        max_value = self.max_val
        value = random.randint(min_value, max_value)
        self.value = value
    
    def __str__(self) -> str:
        return self.parameter


