from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import ProjectForm, TaskForm
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


class ProjectCreate(LoginRequiredMixin, CreateView):
    template_name = "project_form.html"
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        return redirect('project:listview')


class TaskCreate(LoginRequiredMixin, CreateView):
    template_name = "project_form.html"
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        # print(form)
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project:detailview', pk=project.pk)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project_form.html'
    form_class = ProjectForm
    context_key = 'project'

    def get_success_url(self):
        return reverse('project:detailview', kwargs={'pk': self.object.pk})


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'project_form.html'
    form_class = TaskForm
    context_object_name = 'task'
    pk_url_kwarg = 'pk2'

    def get_success_url(self):
        return reverse('project:detail', kwargs={'pk': self.object.project.pk, 'pk2': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('project:listview')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    # template_name = 'task_delete.html'
    # context_object_name = 'task'
    pk_url_kwarg = 'pk2'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project:detailview', kwargs={'pk': self.object.project.pk})

