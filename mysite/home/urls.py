from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import StudentListView
from .views import student_profile


urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:student_id>/', student_profile, name='student_profile'),
    path('', views.home, name='home'),
    path('api/get-quiz/', views.get_quiz, name='get-quiz'),
    path('quiz/', views.quiz, name='quiz'),
    path('do_task/', views.do_task, name='do_task'),
    path('results/', views.results, name='results'),
]
