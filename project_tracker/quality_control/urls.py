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
    path('features/make_request/', views.FeatureCreateView.as_view(), name='feature_request'),
    path('bugs/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='bug_update'),
    # path('bugs/<int:bug_id>/update/', views.update_bug, name='bug_update'),
    path('features/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='feature_update'),
    # path('features/<int:feature_id>/update/', views.update_feature, name='feature_update'),
    # path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='bug_delete'),
    path('bugs/<int:bug_id>/delete/', views.bug_delete, name='bug_delete'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='feature_delete'),
    # path('features/<int:feature_id>/delete/', views.feature_delete, name='feature_delete'),
]
