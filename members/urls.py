from django.urls import path
from . import views

urlpatterns = [
    # PTL urls
    path("ptls/<int:pk>/delete/", views.PhysicalTrainingLeaderDeleteView.as_view(), name="ptl_delete"),
    path("ptls/<int:pk>/edit/", views.PhysicalTrainingLeaderUpdateView.as_view(), name="ptl_edit"),
    path("ptls/<int:pk>/", views.PhysicalTrainingLeaderDetailView.as_view(), name="ptl_detail"),
    path("ptls/new/", views.PhysicalTrainingLeaderCreateView.as_view(), name="ptl_new"),
    path("ptls/", views.PhysicalTrainingLeaderListView.as_view(), name="ptl_list"),

    # UFPM urls
    path("ufpms/<int:pk>/delete/", views.UnitFitnessProgramManagerDeleteView.as_view(), name="ufpm_delete"),
    path("ufpms/<int:pk>/edit/", views.UnitFitnessProgramManagerUpdateView.as_view(), name="ufpm_edit"),
    path("ufpms/<int:pk>/", views.UnitFitnessProgramManagerDetailView.as_view(), name="ufpm_detail"),
    path("ufpms/new/", views.UnitFitnessProgramManagerCreateView.as_view(), name="ufpm_new"),
    path("ufpms/", views.UnitFitnessProgramManagerListView.as_view(), name="ufpm_list"),

    # UFAC urls
    path("ufacs/<int:pk>/delete/", views.UnitFitnessAssessmentCellDeleteView.as_view(), name="ufac_delete"),
    path("ufacs/<int:pk>/edit/", views.UnitFitnessAssessmentCellUpdateView.as_view(), name="ufac_edit"),
    path("ufacs/<int:pk>/", views.UnitFitnessAssessmentCellDetailView.as_view(), name="ufac_detail"),
    path("ufacs/new/", views.UnitFitnessAssessmentCellCreateView.as_view(), name="ufac_new"),
    path("ufacs/", views.UnitFitnessAssessmentCellListView.as_view(), name="ufac_list"),
]
