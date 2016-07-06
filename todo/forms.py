from django import forms

from todo.models import Todo

class TodoForm(forms.ModelForm):
    class Meta(object):
        model = Todo
        fields = ['name', 'description']