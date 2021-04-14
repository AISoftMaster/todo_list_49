from django import forms
from django.forms import CheckboxSelectMultiple
from listapp.models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'created', 'finished')


class ProjectUserForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('users',)
        widgets = {'users': CheckboxSelectMultiple}


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'type', 'status')
