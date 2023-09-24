from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from .views import StudentListView
from .views import student_profile

from .views import CustomLoginView, CustomLogoutView, StudentListView, student_profile, home, get_quiz, quiz, do_task, results
from django.urls import path

urlpatterns = [
<<<<<<< HEAD
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='home'), name='logout'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:student_id>/', student_profile, name='student_profile'),
    path('', home, name='home'),
    path('api/get-quiz/', get_quiz, name='get-quiz'),
    path('quiz/', quiz, name='quiz'),
    path('do_task/', do_task, name='do_task'),
    path('results/', results, name='results'),
=======
    path('', views.home, name='home'),
    path('api/get-quiz/', views.get_quiz, name='get-quiz'),
    path('quiz/', views.quiz, name='quiz'),
    path('do_task/', views.do_task, name='do_task'),
    path('results/', views.results, name='results'),
    path('redo_task/', views.redo_task, name='redo_task'),
>>>>>>> origin/finish_mcq_task
]
