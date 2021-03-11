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
class Task(models.Model):
    title = models.CharField(max_length=350)

    description = models.CharField(max_length=350, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    upgreate = models.DateTimeField(auto_now=True)

    type = models.ForeignKey('listapp.Type', on_delete=models.PROTECT, related_name="tasks")
    status = models.ForeignKey('listapp.Status', on_delete=models.PROTECT, related_name="status")

    def __str__(self):
        return self.title

# class Treker(models.Model):
#     title = models.CharField(max_length=350)

#     status = models.ForeignKey(on_delete=Protect)
#     [type = models.CharField()
