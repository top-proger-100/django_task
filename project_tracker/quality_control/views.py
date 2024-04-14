from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from quality_control.models import BugReport, FeatureRequest
from quality_control.forms import BugReportForm, FeatureRequestForm


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


# create

class BugCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bugs')


def bug_report_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:features')


def feature_request_create(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


# read

class BugListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugs.html'
    context_object_name = 'bug_list'


def bug_list(request):
    bug_report = BugReport.objects.all()
    return render(request, 'quality_control/bugs.html', {'bug_list': bug_report})


class FeatureListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/features.html'
    context_object_name = 'feature_list'


def feature_list(request):
    feature_request = FeatureRequest.objects.all()
    return render(request, 'quality_control/features.html', {'feature_list': feature_request})


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return render(request, 'quality_control/bug_detail.html', {'bug': obj})


def bug_detail_view(request, bug_id):
    obj = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': obj})


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return render(request, 'quality_control/feature_detail.html', {'feature': obj})


def feature_detail_view(request, feature_id):
    obj = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/bug_detail.html', {'feature': obj})


# update

class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    def get_success_url(self):
        return reverse_lazy('quality_control:bug_detail', kwargs={'bug_id': self.object.id})


def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'bug': bug, 'form': form})


class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    def get_success_url(self):
        return reverse_lazy('quality_control:feature_detail', kwargs={'feature_id': self.object.id})


def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'feature': feature, 'form': form})
