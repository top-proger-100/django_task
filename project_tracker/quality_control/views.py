from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from quality_control.models import BugReport


# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bugs')
        feature_list_url = reverse('quality_control:features')
        html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{feature_list_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)


def bug_list(request):
    bug_report = BugReport.objects.all()
    html = f"<h1>Cписок отчетов об ошибках</h1><ul>"
    for record in bug_report:
        html += f'<li><a href="{record.id}">{record.title}</a> | {record.status}</li>'
    html += '</ul>'
    return HttpResponse(html)


def feature_list(request):
    return HttpResponse("<h1>Список запросов на улучшение</h1>")


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        html = f'''
            <h1>Детали бага {obj.id}</h1>
            <p>Название: {obj.title}</p>
            <p>Описание: {obj.description}</p>
            <p>Статус: {obj.status}</p>
            <p>Приоритет: {obj.priority}</p>
            <p>Связанный проект: {obj.project}</p>
            <p>Связанная задача: {obj.task}</p>
        '''
        return HttpResponse(html)


def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")
