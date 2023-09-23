from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import StudentListView
urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list'),
    path('', views.home, name='home'),
    path('api/get-quiz/', views.get_quiz, name='get-quiz'),
    path('quiz/', views.quiz, name='quiz'),
    
]
