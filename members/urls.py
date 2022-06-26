from .views import MemberListView, MemberDetailView
from django.urls import path

urlpatterns = [
    path("<int:pk>/", MemberDetailView.as_view(), name="member_detail"),
    path("", MemberListView.as_view(), name="member_list"),
]
