from django import forms
from django.forms import fields
from .models import Participant


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['email']