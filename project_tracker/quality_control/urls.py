from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='start'),
    path('bugs/', views.bug_list, name='bugs'),
    path('features/', views.feature_list, name='features'),
    path('bugs/<int:bug_id>/', views.bug_detail),
    path('features/<int:feature_id>/', views.feature_detail),
]
