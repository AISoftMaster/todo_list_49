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


class TaskType(models.Model):
    task = models.ForeignKey('listapp.Task', related_name="task_types", on_delete=models.CASCADE, verbose_name='Задача')

    type = models.ForeignKey('listapp.Type', related_name="type_tasks", on_delete=models.CASCADE, verbose_name='Тэг')

    def __str__(self):
        return "{} | {}".format(self.task, self.type)


class Task(models.Model):
    title = models.CharField(max_length=350)

    description = models.CharField(max_length=2048, null=False, blank=False, verbose_name="Описание")
    created = models.DateTimeField(auto_now_add=True)
    upgreate = models.DateTimeField(auto_now=True)

    # type = models.ForeignKey('listapp.Type', on_delete=models.PROTECT, related_name="tasks")
    type = models.ManyToManyField('listapp.Type', through='listapp.TaskType', through_fields=('task', 'type'), related_name="tasks", blank=True)
    status = models.ForeignKey('listapp.Status', on_delete=models.PROTECT, related_name="status")

    def __str__(self):
        return self.title


