from django import forms
from django.db.models import fields
from .models import Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text' , 'votes']

