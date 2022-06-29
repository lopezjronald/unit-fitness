from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UnitFitnessAssessmentCell, UnitFitnessProgramManager, PhysicalTrainingLeader


# PTL views
class PhysicalTrainingLeaderListView(ListView):
    model = PhysicalTrainingLeader
    template_name = "members/ptls/ptl_list.html"
    context_object_name = "ptl_list"
    paginate_by = 5


class PhysicalTrainingLeaderDetailView(DetailView):
    model = PhysicalTrainingLeader
    template_name = "members/ptls/ptl_detail.html"
    context_object_name = "ptl"


class PhysicalTrainingLeaderCreateView(CreateView):
    model = PhysicalTrainingLeader
    template_name = "members/ptls/ptl_new.html"
    fields = ["rank",
              "first_name",
              "middle_name",
              "last_name",
              "phone_number",
              "email",
              "cpr_card",
              "ptl_completion_date",
              "appointment_letter"]


class PhysicalTrainingLeaderUpdateView(UpdateView):
    model = PhysicalTrainingLeader
    template_name = "members/ptls/ptl_edit.html"
    fields = (
        "rank",
        "first_name",
        "middle_name",
        "last_name",
        "phone_number",
        "email",
        "cpr_card",
        "ptl_completion_date",
        "appointment_letter",
    )


class PhysicalTrainingLeaderDeleteView(DeleteView):
    model = PhysicalTrainingLeader
    template_name = "members/ptls/ptl_delete.html"
    success_url = reverse_lazy("ptl_list")


# UFPM views
class UnitFitnessProgramManagerListView(ListView):
    model = UnitFitnessProgramManager
    template_name = "members/ufpms/ufpm_list.html"
    context_object_name = "ufpm_list"
    paginate_by = 5


class UnitFitnessProgramManagerDetailView(DetailView):
    model = UnitFitnessProgramManager
    template_name = "members/ufpms/ufpm_detail.html"
    context_object_name = "ufpm"


class UnitFitnessProgramManagerCreateView(CreateView):
    model = UnitFitnessProgramManager
    template_name = "members/ufpms/ufpm_new.html"
    fields = ["rank",
              "first_name",
              "middle_name",
              "last_name",
              "phone_number",
              "email",
              "ufpm_completion_date",
              "appointment_letter",
              "written_order"]


class UnitFitnessProgramManagerUpdateView(UpdateView):
    model = UnitFitnessProgramManager
    template_name = "members/ufpms/ufpm_edit.html"
    fields = (
        "rank",
        "first_name",
        "middle_name",
        "last_name",
        "phone_number",
        "email",
        "ufpm_completion_date",
        "appointment_letter",
        "written_order",
    )


class UnitFitnessProgramManagerDeleteView(DeleteView):
    model = UnitFitnessProgramManager
    template_name = "members/ufpms/ufpm_delete.html"
    success_url = reverse_lazy("ufpm_list")


# UFAC views
class UnitFitnessAssessmentCellListView(ListView):
    model = UnitFitnessAssessmentCell
    template_name = "members/ufacs/ufac_list.html"
    context_object_name = "ufac_list"
    paginate_by = 5


class UnitFitnessAssessmentCellDetailView(DetailView):
    model = UnitFitnessAssessmentCell
    template_name = "members/ufacs/ufac_detail.html"
    context_object_name = "ufac"


class UnitFitnessAssessmentCellCreateView(CreateView):
    model = UnitFitnessAssessmentCell
    template_name = "members/ufacs/ufac_new.html"
    fields = ["physical_training_leader",
              "ufac_completion_date",
              "system_authorization_request",
              "written_order",
              "user_agreement"]


class UnitFitnessAssessmentCellUpdateView(UpdateView):
    model = UnitFitnessAssessmentCell
    template_name = "members/ufacs/ufac_edit.html"
    fields = ("physical_training_leader",
              "ufac_completion_date",
              "system_authorization_request",
              "written_order",
              "user_agreement",
              )


class UnitFitnessAssessmentCellDeleteView(DeleteView):
    model = UnitFitnessAssessmentCell
    template_name = "members/ufacs/ufac_delete.html"
    success_url = reverse_lazy("ufac_list")
