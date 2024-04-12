from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='start'),
    path('bugs/', views.bug_list, name='bugs'),
    path('features/', views.feature_list, name='features'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view()),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view()),
]
