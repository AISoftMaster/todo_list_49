from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import ProjectForm, TaskForm, ProjectUserForm
from .models import Task, Project


# Create your views here.

class TaskListview(ListView):
    template_name = "task_list.html"
    context_object_name = "tasks"
    model = Task
    paginate_by = 5


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task_detailview.html"
    pk_url_kwarg = "pk2"


class ProjectListview(ListView):
    template_name = "project_listview.html"
    context_object_name = "projects"
    model = Project
    paginate_by = 5


class ProjectsDetailView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "project_detailview.html"


class ProjectCreate(PermissionRequiredMixin, CreateView):
    template_name = "project_form.html"
    model = Project
    form_class = ProjectForm
    permission_required = ('listapp.add_project',)

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        return redirect('project:listview')


class TaskCreate(PermissionRequiredMixin, CreateView):
    template_name = "project_form.html"
    model = Task
    form_class = TaskForm
    permission_required = ('listapp.add_task',)

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.users.all()

    def form_valid(self, form):
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project:detailview', pk=project.pk)


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'project_form.html'
    form_class = ProjectForm
    context_key = 'project'
    permission_required = ('listapp.change_project',)

    def get_success_url(self):
        return reverse('project:detailview', kwargs={'pk': self.object.pk})


class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    model = Task
    template_name = 'project_form.html'
    form_class = TaskForm
    context_object_name = 'task'
    pk_url_kwarg = 'pk2'
    permission_required = ('listapp.change_task',)

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.users.all()

    def get_success_url(self):
        return reverse('project:detail', kwargs={'pk': self.object.project.pk, 'pk2': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('project:listview')
    permission_required = ('listapp.delete_project',)


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    model = Task
    pk_url_kwarg = 'pk2'
    permission_required = ('listapp.delete_task',)

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.users.all()

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project:detailview', kwargs={'pk': self.object.project.pk})


class ProjectUsersDetail(PermissionRequiredMixin, UpdateView):
    model = Project
    context_object_name = 'project'
    template_name = 'project_users.html'
    permission_required = ('listapp.can_add_user',)
    form_class = ProjectUserForm

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()

    def get_success_url(self):
        return reverse('project:detailview', kwargs={'pk': self.object.pk})
