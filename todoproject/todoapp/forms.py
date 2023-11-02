from django import forms
from .models import Task  # Import your Task model or adjust the import path as needed

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task  # Specify the model class here
        fields = ['name', 'priority', 'date']  # Specify the fields you want in the form
