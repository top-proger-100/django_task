from django.contrib import admin

from .models import BugReport, FeatureRequest


# Register your models here.


@admin.register(BugReport)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'created_at', 'updated_at', 'priority')
    list_filter = ('status', 'task', 'project')
    search_fields = ('title', 'description')


@admin.register(FeatureRequest)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'created_at', 'updated_at', 'priority')
    list_filter = ('status', 'task', 'project')
    search_fields = ('title', 'description')
