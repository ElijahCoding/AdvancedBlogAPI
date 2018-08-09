from django import forms
from .models import Todo

class TodoForm(forms.Form):
    text = forms.CharField(max_length=120,
                           widget=forms.TextInput(
                               attrs={'class':'form-control', 'placeholder':'Enter Todo'}
                           ))

class NewTodoForm(forms.Form):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Enter Todo'}
            )
        }
