from .models import Task, Tag
from django import forms
from django.forms import Form, ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['user', 'task', 'tags']
        template_name = 'tasks.html'

    tags = ModelMultipleChoiceField(
    queryset=Tag.objects.all(),
    widget=CheckboxSelectMultiple(), required=False,
    )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)