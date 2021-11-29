from django import forms
from .models import Poll

class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']
        widgets = {
            'question' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 3}),
            'option_one' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter option 1'}),
            'option_two' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter option 2'}),
            'option_three' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter option 3'}),
        }