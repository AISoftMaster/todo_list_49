from django.contrib import admin
from .models import Task, Status, Type, Project, ProjectUser

# Register your models here.
admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)
admin.site.register(ProjectUser)
