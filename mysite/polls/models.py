import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

import sympy
import random


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (0, 'professor'),
        (1, 'student'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

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


class NumericQuestion(models.Model):
    def __str__(self):
        return self.question_text
    
    #Variables es una lista con las variables x,y,z
    variables = models.CharField(max_length=30)
    question_text = models.CharField(max_length=200)
    difficulty = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], default=1)

    def generate_question(question_text,variables)




class Equation(models.Model):
    def __str__(self):
        return self.question_text
    
    def solve_equation(equation):
        # Parse the equation
        expr = sympy.sympify(equation)
        
        # Find all variables in the equation
        variables = list(expr.free_symbols)
        
        # Generate a random value for each variable
        variable_values = {var: random.randint(1, 10) for var in variables}
        
        # Substitute the variable values into the equation and evaluate it
        solution = expr.subs(variable_values)
        
        # Return the solution and the variable values
        return solution, variable_values

    equation = models.CharField(max_length=200)

    # pub_date = models.DateTimeField('date published')
    # difficulty = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], default=1)
    # answer = models.CharField(max_length=200)


