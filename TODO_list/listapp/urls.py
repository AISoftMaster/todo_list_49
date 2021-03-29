from django.urls import path
from . import views
from .views import TaskListview, ProjectListview, ProjectsDetailView, ProjectCreate, TaskCreate

urlpatterns = [
    path('listapp/', views.index, name="index"),
    path('<int:pk>/task/', TaskListview.as_view(), name='task_list'),
    path('<int:pk>/task/create/', TaskCreate.as_view(), name='task_create'),
    path('', ProjectListview.as_view(), name='project_listview'),
    path('<int:pk>/', ProjectsDetailView.as_view(), name='project_detailview'),
    path('create/', ProjectCreate.as_view(), name='project_create')
    # path('task/<int:pk>', ProjectCreate)
]
