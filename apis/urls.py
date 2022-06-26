from django.urls import path
from .views import MemberAPIView

urlpatterns = [
    path("members/", MemberAPIView.as_view(), name="api_member_list"),
]
