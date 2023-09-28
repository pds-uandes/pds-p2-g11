from django.db import models
import uuid
# Create your models here.
import random
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
from django.contrib.postgres.fields import JSONField
from sympy import sin, evalf, pi, sympify

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    JSON_FIELD_USER = {
        'difficulty': 1, # 1: easy, 2: medium, 3: hard, 4:DINAMIC 1 5:DINAMIC 2
        'theme': 1}
    JSON_FIELD_SCORE = {
    'tasks' : 0,

    'level1' : {
        'wrongs': 0,
        'correct': 0,
    },
    'level2' : {
        'wrongs': 0,
        'correct': 0,
    },

    'level3' : {
        'wrongs': 0,
        'correct': 0,
    },

        'level4' : {
        'wrongs': 0,
        'correct': 0,
    },

        'level5' : {
        'wrongs': 0,
        'correct': 0,
    }
    }

    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    total_time_spent = models.DurationField(default=timedelta())

    json_user = models.JSONField(default=JSON_FIELD_USER)
    user_score = models.JSONField(default=JSON_FIELD_SCORE)

    last_task = models.ForeignKey('Task', related_name='user_last_task', on_delete=models.CASCADE, null=True, blank=True)

    def get_accuracy_and_lowest_topic(self):
        accuracies = {}
        min_accuracy = 100
        topic_with_lowest_accuracy = None
        theme_names = {1: 'Caracteristicas de la onda', 2: 'Ondas Sonoras', 3: 'Ondas Armonicas', 4: 'Ecuacion de la Onda', 5: 'Energias e info. transferida'}
        for theme in range(1, 6):  # Assuming themes are numbered from 1 to 5
            total = self.user_score[f'level{theme}']['wrongs'] + self.user_score[f'level{theme}']['correct']
            if total == 0:
                accuracies[theme] = "Not enough info"
            else:
                accuracy = (self.user_score[f'level{theme}']['correct'] / total) * 100
                accuracies[theme] = accuracy
                if accuracy < min_accuracy:
                    min_accuracy = accuracy
                    topic_with_lowest_accuracy = theme_names[theme]

        if topic_with_lowest_accuracy is None:
            topic_with_lowest_accuracy = "Not enough info"

        return topic_with_lowest_accuracy

    def get_time_per_task(self):
        print("TOTALTIMESPTEN")
        print(type(self.total_time_spent))
        total_time = self.total_time_spent.total_seconds()/60
        return total_time/int(self.user_score['tasks'])

    def get_time_per_level(self):
        total_time = self.total_time_spent.total_seconds()/60
        level =  int(self.json_user['theme'])
        return level/total_time
    


class Task(BaseModel):
    tries = {
        'first_try_answered': False,
        'second_try': False,
        'second_try_answered': False,
        'user_answered': False,
    }
    redos = 0
    wrongs = []
    wrongs_permanent = []
    questions = []
    counter = models.IntegerField(default=0)
    wrongs_counter = models.IntegerField(default=-1)
    score = models.IntegerField(default=0)
    dinamic_counter = 1
    def __str__(self) -> str:
        return f"Task - {self.uid}"

    def update_score(self, score):
        self.score = score
        self.save()

    def update_trys(self, parameter):
        self.trys[parameter] = True
        self.save()

    def add_question(self, theme, difficulty):

        if difficulty < 4:
            question_query = Q(difficulty=difficulty) & Q(theme=theme)
            question = Question.objects.filter(question_query).order_by('?').first()
            return question

        # 1: easy, 2: medium, 3: hard, 4:DINAMIC 1 5:DINAMIC 2
        if difficulty == 4:
            question_query = Q(difficulty=1) & Q(theme=theme)
            question = DinamicQuestion.objects.filter(question_query).order_by('?').first()
            return question
        if difficulty == 5:
            question_query = Q(difficulty=2) & Q(theme=theme)
            question = DinamicQuestion.objects.filter(question_query).order_by('?').first()
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
    question_text = models.CharField(max_length=1000)
    hint = models.CharField(max_length=200, null=True, blank=True)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)
    theme = models.IntegerField(choices=THEME_CHOICES, default=1)
    user_answer = ''
    real_answer = ''

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
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer

# ===================== NUMERIC =====================
class DinamicQuestion(BaseModel):
    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2, 'Medium'),]

    THEME_CHOICES = [
        (1, 'Caracteristicas de la onda'),
        (2, 'Ondas Sonoras'),
        (3, 'Ondas Armonicas'),
        (4, 'Ecuacion de la Onda'),
        (5, 'Energias e Info. Transferida')]

    dic = {"[VELOCIDAD]": 0,
            "[TIEMPO]": 0,
            "[DISTANCIA]": 0,
            '[FRECUENCIA]': 0,
            '[LONGITUD]': 0,
            '[PERIODO]': 0,
            '[AMPLITUD]': 0,
            '[NODOS]': 0,
            '[DENSIDAD]':0,
            '[RANDOM]':0,}

    task = models.ForeignKey(Task, related_name='dinamic_task_questions', on_delete=models.CASCADE, null=True, blank=True)

    question_text = models.CharField(max_length=1000)
    hint = models.CharField(max_length=200, null=True, blank=True)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)
    theme = models.IntegerField(choices=THEME_CHOICES, default=1)
    wrong_answers = []

    def __str__(self) -> str:
        return self.question_text

    def fill_answers(self):
        answer_objs = list(DinamicAnswer.objects.filter(question = self))
        for answer in answer_objs:
            for parameter in self.parameters:
                answer.dic[parameter.parameter] = parameter.value
            answer.equation_value()
            answer.save()

    def generate_random_parameters(self):
        parameters_objs = list(Parameters.objects.filter(question=self))
        self.parameters = parameters_objs
        for parameter in parameters_objs:
            parameter.generate_random_value()
            parameter.save()

    def replace_parameters(self):
        self.generate_random_parameters()
        self.fill_answers()
        replaced_text = self.question_text
        for parameter in self.parameters:
            replaced_text = replaced_text.replace(parameter.parameter, str(parameter.value))
            self.dic[parameter.parameter] = parameter.value
        self.replaced_text = replaced_text

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
    question = models.ForeignKey(DinamicQuestion,related_name='dinamic_question_answer', on_delete=models.CASCADE)

    dic = {"[VELOCIDAD]": 0,
            "[TIEMPO]": 0,
            "[DISTANCIA]": 0,
            '[FRECUENCIA]': 0,
            '[LONGITUD]': 0,
            '[PERIODO]': 0,
            '[AMPLITUD]': 0,
            '[NODOS]': 0,
            '[DENSIDAD]':0,
            '[RANDOM]':0,}

    metrics = models.CharField(max_length=100)
    equation = models.CharField(max_length=1000, blank=True)
    hint = models.CharField(max_length=200, blank=True)
    user_answer = 0

    def __str__(self) -> str:
        return self.equation

    def equation_value(self):
        self.aux_equation = self.equation
        for placeholder, value in self.dic.items():
            self.equation = self.equation.replace(placeholder, str(value))
        
        #result = eval(self.equation)
        result = sympify(self.equation)
        result = result.evalf()
        self.result = [round(result) - round(result, 3)*0.05, round(result, 3) + round(result, 3)*0.05]
        self.equation = self.aux_equation

    def get_result(self):
        self.aux_equation = self.equation
        for placeholder, value in self.dic.items():
            self.equation = self.equation.replace(placeholder, str(value))
        result = eval(self.equation)
        result = [round(result,3) - round(result*0.05, 3), round(result, 3) + round(result*0.05, 3)]
        self.equation = self.aux_equation
        self.result = result
        return result

class Parameters(BaseModel):
    question = models.ForeignKey(DinamicQuestion,related_name='dinamic_question_parameters', on_delete=models.CASCADE)
    parameter = models.CharField(max_length=100)
    min_val = models.IntegerField(default=0)
    max_val = models.IntegerField(default=0)

    def generate_random_value(self, *args, **kwargs):
        self.value = random.randint(self.min_val, self.max_val)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.parameter


