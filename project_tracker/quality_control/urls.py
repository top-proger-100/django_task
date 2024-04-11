from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    path('another/', views.another_page, name='another_page'),
]
