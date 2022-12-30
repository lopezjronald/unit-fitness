from django.urls import path
from .views import ExemptionFormView

app_name = "memos"

urlpatterns = [
    path("exemptions/", ExemptionFormView.as_view(), name="exemption"),
]
