from django.urls import path
from .views import (AssessmentListView,
                    AssessmentDetailView,
                    AssessmentCreateView,
                    AssessmentUpdateView,
                    AssessmentDeleteView)

urlpatterns = [
    path("<int:pk>/delete/", AssessmentDeleteView.as_view(), name="assessment_delete"),
    path("<int:pk>/edit/", AssessmentUpdateView.as_view(), name="assessment_edit"),
    path("new/", AssessmentCreateView.as_view(), name="assessment_new"),
    path("<int:pk>/", AssessmentDetailView.as_view(), name="assessment_detail"),
    path("", AssessmentListView.as_view(), name="assessment_list"),
]
