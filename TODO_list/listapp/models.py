from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=350)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=350)

    def __str__(self):
        return self.name
# Create your models here.


class Project(models.Model):
    created = models.DateTimeField()
    finished = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=250)

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

    def __str__(self):
        return self.title


