from django.urls import path
from . import views
from .views import TaskListview

urlpatterns = [
    path('', views.index, name="index"),
    path('task/', TaskListview.as_view(), name='task_list'),
]
