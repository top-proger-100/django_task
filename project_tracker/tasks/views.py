from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def index(request):
    another_page_url = reverse('tasks:another_page')
    quality_control_page_url = reverse('quality_control:start')
    html = (f"<h1>Страница приложения tasks</h1><a href='{another_page_url}'>Перейти на другую страницу</a><br>"
            f"<a href='{quality_control_page_url}'>Перейти на страницу приложения quality_control</a>")
    return HttpResponse(html)


def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")
