from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UnitFitnessAssessmentCell, UnitFitnessProgramManager, PhysicalTrainingLeader, SpecialMember

# Special Member views
class SpecialMemberListView(LoginRequiredMixin, ListView):
    model = SpecialMember
    template_name = "members/special_members/special_member_list.html"
    context_object_name = "special_member_list"

class SpecialMemberDetailView(LoginRequiredMixin, DetailView):
    model = SpecialMember
    template_name = "members/special_members/special_member_detail.html"
    context_object_name = "special_member"

# PTL views
class PhysicalTrainingLeaderListView(LoginRequiredMixin, ListView):
    model = PhysicalTrainingLeader
    template_name = "members/ptls/ptl_list.html"
    context_object_name = "ptl_list"
    paginate_by = 5


class PhysicalTrainingLeaderDetailView(LoginRequiredMixin, DetailView):
    model = PhysicalTrainingLeader
    template_name = "members/ptls/ptl_detail.html"
    context_object_name = "ptl"


class PhysicalTrainingLeaderCreateView(LoginRequiredMixin, CreateView):
    model = PhysicalTrainingLeader
    template_name = "members/ptls/ptl_new.html"
    fields = ["rank",
              "first_name",
              "middle_name",
              "last_name",
              "phone_number",
              "email",
              "cpr_card",
              "cpr_expiration_date",
              "ptl_completion_date",
              "appointment_letter"]


class PhysicalTrainingLeaderUpdateView(LoginRequiredMixin, UpdateView):
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
        "cpr_expiration_date",
        "ptl_completion_date",
        "appointment_letter",
    )


class PhysicalTrainingLeaderDeleteView(LoginRequiredMixin, DeleteView):
    model = PhysicalTrainingLeader
    template_name = "members/ptls/ptl_delete.html"
    success_url = reverse_lazy("ptl_list")


# UFPM views
class UnitFitnessProgramManagerListView(LoginRequiredMixin, ListView):
    model = UnitFitnessProgramManager
    template_name = "members/ufpms/ufpm_list.html"
    context_object_name = "ufpm_list"
    paginate_by = 5


class UnitFitnessProgramManagerDetailView(LoginRequiredMixin, DetailView):
    model = UnitFitnessProgramManager
    template_name = "members/ufpms/ufpm_detail.html"
    context_object_name = "ufpm"


class UnitFitnessProgramManagerCreateView(LoginRequiredMixin, CreateView):
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


class UnitFitnessProgramManagerUpdateView(LoginRequiredMixin, UpdateView):
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


class UnitFitnessProgramManagerDeleteView(LoginRequiredMixin, DeleteView):
    model = UnitFitnessProgramManager
    template_name = "members/ufpms/ufpm_delete.html"
    success_url = reverse_lazy("ufpm_list")


# UFAC views
class UnitFitnessAssessmentCellListView(LoginRequiredMixin, ListView):
    model = UnitFitnessAssessmentCell
    template_name = "members/ufacs/ufac_list.html"
    context_object_name = "ufac_list"
    paginate_by = 5


class UnitFitnessAssessmentCellDetailView(LoginRequiredMixin, DetailView):
    model = UnitFitnessAssessmentCell
    template_name = "members/ufacs/ufac_detail.html"
    context_object_name = "ufac"


class UnitFitnessAssessmentCellCreateView(LoginRequiredMixin, CreateView):
    model = UnitFitnessAssessmentCell
    template_name = "members/ufacs/ufac_new.html"
    fields = ["physical_training_leader",
              "ufac_completion_date",
              "system_authorization_request",
              "written_order",
              "user_agreement"]


class UnitFitnessAssessmentCellUpdateView(LoginRequiredMixin, UpdateView):
    model = UnitFitnessAssessmentCell
    template_name = "members/ufacs/ufac_edit.html"
    fields = ("physical_training_leader",
              "ufac_completion_date",
              "system_authorization_request",
              "written_order",
              "user_agreement",
              )


class UnitFitnessAssessmentCellDeleteView(LoginRequiredMixin, DeleteView):
    model = UnitFitnessAssessmentCell
    template_name = "members/ufacs/ufac_delete.html"
    success_url = reverse_lazy("ufac_list")
