from django.db.models.fields import DateTimeField
from django.forms.fields import CharField
from django.forms.widgets import TextInput
from django.utils.timezone import localtime, now
from django.db.models.base import ModelState
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