from django.urls import path
from .views import StudentListView
from .views import student_profile
from .views import CustomLoginView, CustomLogoutView, StudentListView, student_profile, home, get_quiz, quiz, do_task, results, question_view, add_question_view,edit_question_view,delete_question_view,add_question_view

from django.urls import path
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='home'), name='logout'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:student_id>/', student_profile, name='student_profile'),
    path('', home, name='home'),
    path('api/get-quiz/', get_quiz, name='get-quiz'),
    path('quiz/', quiz, name='quiz'),
    path('do_task/', do_task, name='do_task'),
    path('results/', results, name='results'),
    path('redo_task/', views.redo_task, name='redo_task'),
    path('questions/', question_view, name='questions'),
    path('questions/add/', add_question_view, name='add_question'),
    path('questions/edit/<uuid:pk>/', edit_question_view, name='edit_question'),
    path('questions/delete/<uuid:pk>/', delete_question_view, name='delete_question'),
    path('questions/add/', add_question_view, name='add_question'),
    
]
