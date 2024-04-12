from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Project, Task


# Create your views here.


def index(request):
    # projects_list_url = reverse('tasks:projects_list')
    # html = f"<h1>Страница приложения tasks</h1><a href='{projects_list_url}'>Список проектов</a>"
    # return HttpResponse(html)
    return render(request, 'tasks/index.html')


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')


def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'project_list': projects})


class ProjectsListView(ListView):
    model = Project
    template_name = 'tasks/projects_list.html'


def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'tasks/project_detail.html', {'project': project})


class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    template_name = 'tasks/project_detail.html'


def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    return render(request, 'tasks/task_detail.html', {'task': task})


class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'
