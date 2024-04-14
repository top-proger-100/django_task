from django.contrib import admin

from .models import BugReport, FeatureRequest


# Register your models here.

class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'description', 'project', 'task', 'status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True


class FeatureRequestInline(admin.TabularInline):
    model = FeatureRequest
    extra = 0
    fields = ('title', 'description', 'project', 'task', 'status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'created_at', 'updated_at', 'priority')
    list_filter = ('status', 'task', 'project')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'created_at', 'updated_at', 'priority')
    list_filter = ('status', 'task', 'project')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
