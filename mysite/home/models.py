from django.db import models
import uuid
# Create your models here.
import random
from django.db.models import Q


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Task(BaseModel):
    tries = {
        'first_try_answered': False, # true
        'second_try': False, # score 5/5 o 100% de las preguntas = True
        'second_try_answered': False, # ""
    }

    counter = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Task - {self.uid}"

    def update_score(self, score):
        self.score = score
        self.save()

    def update_trys(self, parameter):
        self.trys[parameter] = True
        self.save()

    def add_questions(self, level, task_type, difficulty):
        if level == 0:
            theme = 1

        question_query = Q(difficulty=difficulty) & Q(theme=theme)
        # type 0: multiple choice questions
        # type 1: numeric question
        if task_type == 0:
            questions = Question.objects.filter(question_query).order_by('?')[:5]

        # Assign the questions to the task
            for question in questions:
                question.task = self
                question.save()

            return questions

    def generate_question(self):
        #No hay mas preguntas se va a results page
        #Segun el json que tiene te entrega una de las preguntas

        if self.counter == 5:
            return False


        return True



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
