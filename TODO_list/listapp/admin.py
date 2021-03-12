from django.contrib import admin
from .models import Task, Status, Type

# Register your models here.
admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Status)
