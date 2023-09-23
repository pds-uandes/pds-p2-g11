from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('api/get-quiz/', views.get_quiz, name='get-quiz'),
    path('quiz/', views.quiz, name='quiz'),
    path('do_task/', views.do_task, name='do_task'),
    path('results/', views.results, name='results'),
    path('redo_task/', views.redo_task, name='redo_task'),
]
