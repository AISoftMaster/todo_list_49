from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView


from .forms import ProjectForm, TaskForm
from .models import Task, Project, Type


# Create your views here.


def index(request):
    return render(request, "index.html")


class TaskListview(ListView):
    template_name = "task_list.html"
    context_object_name = "tasks"
    model = Task
    paginate_by = 10


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task_detailview.html"
    pk_url_kwarg = "pk2"


class ProjectListview(ListView):
    template_name = "project_listview.html"
    context_object_name = "projects"
    model = Project
    paginate_by = 10


class ProjectsDetailView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "project_detailview.html"


class ProjectCreate(CreateView):
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


        # for t in self.request.POST.get("type"):
        #     TaskType.objects.create(task=task, type=Type.objects.get(pk=int(t)))

        return redirect('project_detailview', pk=project.pk)




