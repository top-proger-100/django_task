from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def index(request):
    bug_list_url = reverse('quality_control:bugs')
    feature_list_url = reverse('quality_control:features')
    html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><a href='{feature_list_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)


def bug_list(request):
    return HttpResponse("<h1>Cписок отчетов об ошибках</h1>")


def feature_list(request):
    return HttpResponse("<h1>Список запросов на улучшение</h1>")
