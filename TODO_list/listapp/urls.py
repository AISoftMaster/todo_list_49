from django.urls import path
from . import views
from .views import TaskListview, ProjectListview, ProjectsDetailView, ProjectCreate, TaskCreate, TaskDetailView, \
    ProjectUpdateView, ProjectDeleteView, TaskUpdateView, TaskDeleteView

app_name = 'project'

urlpatterns = [
    path('<int:pk>/task/<int:pk2>/', TaskDetailView.as_view(), name='detail'),
    path('<int:pk>/task/create/', TaskCreate.as_view(), name='create'),
    path('', ProjectListview.as_view(), name='listview'),
    path('<int:pk>/', ProjectsDetailView.as_view(), name='detailview'),
    path('create/', ProjectCreate.as_view(), name='create'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete'),
    path('<int:pk>/task/<int:pk2>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/task/<int:pk2>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
