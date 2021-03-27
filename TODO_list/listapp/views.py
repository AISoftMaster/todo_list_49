from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from .models import Task


# Create your views here.


def index(request):
    return render(request, "index.html")


class TaskListview(ListView):
    template_name = "task_list.html"
    context_object_name = "tasks"
    model = Task
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
