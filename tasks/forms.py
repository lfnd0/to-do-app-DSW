from django import forms

from .models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description']
        labels = {
            'description': 'Descrição'
        }
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control mt-1 mb-2', 'rows': '3', 'placeholder': 'Digite a sua tarefa'})
        }
