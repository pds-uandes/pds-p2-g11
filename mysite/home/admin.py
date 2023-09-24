from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task, Question, Answer, DinamicQuestion, DinamicAnswer, Parameters

class AnswerInline(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class TaskAdmin(admin.ModelAdmin):
    pass

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_teacher', 'is_student', 'name', 'second_name')
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_teacher', 'is_student', 'name', 'second_name')}),
    )

class DinamicAnswerInline(admin.StackedInline):
    model = DinamicAnswer

class ParametersInline(admin.StackedInline):
    model = Parameters

class DinamicQuestionAdmin(admin.ModelAdmin):
    inlines = [DinamicAnswerInline, ParametersInline]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(DinamicQuestion, DinamicQuestionAdmin)
