from django.db import models
from  django.conf import settings
from django.contrib.auth import get_user_model


class Type(models.Model):
    name = models.CharField(max_length=350)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=350)

    def __str__(self):
        return self.name
# Create your models here.


class ProjectUser(models.Model):
    project = models.ForeignKey('listapp.project', related_name='project_users', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='user_projects', on_delete=models.CASCADE)


class Project(models.Model):
    created = models.DateField()
    finished = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    # author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='projects')
    users = models.ManyToManyField('auth.User', related_name='projects', through='listapp.ProjectUser',
                                   through_fields=('project', 'user'), blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=350)
    description = models.CharField(max_length=2048, null=False, blank=False, verbose_name="Описание")
    created = models.DateTimeField(auto_now_add=True)
    upgreate = models.DateTimeField(auto_now=True)
    type = models.ManyToManyField('listapp.Type', related_name="tasks", blank=True)
    status = models.ForeignKey('listapp.Status', on_delete=models.PROTECT, related_name="status")
    project = models.ForeignKey('listapp.Project', related_name='task_project', on_delete=models.CASCADE, verbose_name='проект')
    # author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='tasks')

    def __str__(self):
        return self.title
