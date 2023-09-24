from django.db import models
import uuid
# Create your models here.
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
