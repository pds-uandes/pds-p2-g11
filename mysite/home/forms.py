from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Question
from django.forms import inlineformset_factory
from .models import Question, Answer

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name', 'second_name')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'hint', 'difficulty', 'theme']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'is_correct']

QuestionFormSet = inlineformset_factory(Question, Answer, form=AnswerForm, extra=1)
AnswerFormSet = inlineformset_factory(Question, Answer, form=AnswerForm, extra=4, max_num=4, can_delete=True)

