from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Assessment


class AssessmentListView(LoginRequiredMixin, ListView):
    model = Assessment
    template_name = "assessments/assessment_list.html"
    context_object_name = "assessment_list"


class AssessmentDetailView(LoginRequiredMixin, DetailView):
    model = Assessment
    template_name = "assessments/assessment_detail.html"
    context_object_name = "assessment"


class AssessmentCreateView(LoginRequiredMixin, CreateView):
    model = Assessment
    template_name = "assessments/assessment_new.html"
    fields = ["date", "time"]


class AssessmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Assessment
    fields = (
        "date",
        "time",
    )
    template_name = "assessments/assessment_edit.html"


class AssessmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Assessment
    template_name = "assessments/assessment_delete.html"
    success_url = reverse_lazy("assessment_list")
