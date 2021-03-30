from django.urls import path
from . import views
from .views import TaskListview, ProjectListview, ProjectsDetailView, ProjectCreate, TaskCreate, TaskDetailView, \
    ProjectUpdateView, ProjectDeleteView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('listapp/', views.index, name="index"),
    # path('<int:pk>/task/', TaskListview.as_view(), name='task_list'),
    # path('<int:pk>/task/', TaskListview.as_view(), name='task_list'),
    path('<int:pk>/task/<int:pk2>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/task/create/', TaskCreate.as_view(), name='task_create'),
    path('', ProjectListview.as_view(), name='project_listview'),
    path('<int:pk>/', ProjectsDetailView.as_view(), name='project_detailview'),
    path('create/', ProjectCreate.as_view(), name='project_create'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('<int:pk>/task/<int:pk2>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/task/<int:pk2>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
