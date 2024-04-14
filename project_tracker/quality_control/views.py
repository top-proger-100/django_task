from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from quality_control.models import BugReport, FeatureRequest
from quality_control.forms import BugReportForm, FeatureRequestForm



# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


def bug_list(request):
    bug_report = BugReport.objects.all()
    return render(request, 'quality_control/bugs.html', {'bug_list': bug_report})


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return render(request, 'quality_control/bug_detail.html', {'bug': obj})


def feature_list(request):
    feature_request = FeatureRequest.objects.all()
    return render(request, 'quality_control/features.html', {'feature_list': feature_request})


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return render(request, 'quality_control/feature_detail.html', {'feature': obj})


def bug_report_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


def feature_request_create(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})
