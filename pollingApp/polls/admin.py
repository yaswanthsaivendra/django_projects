from django.contrib import admin
from .models import Question, Choice
from django.contrib.admin import ModelAdmin

# Register your models here.

class QuestionAdmin(ModelAdmin):
    list_display = ['id', 'question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
