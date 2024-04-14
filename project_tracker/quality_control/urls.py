from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='start'),
    # path('bugs/', views.bug_list, name='bugs'),
    path('bugs/', views.BugListView.as_view(), name='bugs'),
    # path('features/', views.feature_list, name='features'),
    path('features/', views.FeatureListView.as_view(), name='features'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    # path('bugs/<int:bug_id>/', views.bug_detail_view, name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    # path('features/<int:feature_id>/', views.feature_detail_view, name='feature_detail'),
    # path('bugs/make_report/', views.bug_report_create, name='bug_report'),
    # path('features/make_request/', views.feature_request_create, name='feature_request')
    path('bugs/make_report/', views.BugCreateView.as_view(), name='bug_report'),
    path('features/make_request/', views.FeatureCreateView.as_view(), name='feature_request')
]
