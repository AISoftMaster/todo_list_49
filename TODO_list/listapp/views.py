from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.mixins import LoginRequiredMixin


from .forms import ProjectForm, TaskForm
from .models import Task, Project, Type


# Create your views here.

def index(request):
    return render(request, "index.html")


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
        return redirect('project_listview')




class TaskCreate(CreateView):
    template_name = "project_form.html"
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        print(form)
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()

        return redirect('project_detailview', pk=project.pk)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project_form.html'
    form_class = ProjectForm
    context_key = 'project'

    def get_success_url(self):
        return reverse('project_detailview', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'project_form.html'
    form_class = TaskForm
    context_object_name = 'task'
    pk_url_kwarg = 'pk2'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.project.pk, 'pk2': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('project_listview')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
    model = Task
    # template_name = 'task_delete.html'
    # context_object_name = 'task'
    pk_url_kwarg = 'pk2'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project_detailview', kwargs={'pk': self.object.project.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

