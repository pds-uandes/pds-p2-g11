import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    difficulty = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], default=1)

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)



