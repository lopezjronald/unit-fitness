from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from .models import Assessment
from .forms import TesterForm


class AssessmentListView(LoginRequiredMixin, ListView):
    model = Assessment
    template_name = "assessments/assessment_list.html"
    context_object_name = "assessment_list"


class AssessmentDetailView(LoginRequiredMixin, DetailView):
    def get(self, request, *args, **kwargs):
        view = TesterGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = TesterPost.as_view()
        return view(request, *args, **kwargs)


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


class TesterGet(DetailView):
    model = Assessment
    template_name = "assessments/assessment_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TesterForm
        return context


class TesterPost(SingleObjectMixin, FormView):
    model = Assessment
    form_class = TesterForm
    template_name = "assessments/assessment_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        tester = form.save(commit=False)
        tester.assessment = self.object
        tester.save()
        return super().form_valid(form)

    def get_success_url(self):
        assessment = self.get_object()
        return reverse("assessment_detail", kwargs={"pk": assessment.pk})
