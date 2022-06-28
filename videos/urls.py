from .views import (VideoListView,
                    VideoDetailView,
                    VideoCreateView,
                    VideoUpdateView,
                    VideoDeleteView)
from django.urls import path

urlpatterns = [
    path("<int:pk>/delete/", VideoDeleteView.as_view(), name="video_delete"),
    path("<int:pk>/edit/", VideoUpdateView.as_view(), name="video_edit"),
    path("new/", VideoCreateView.as_view(), name="video_new"),
    path("<int:pk>/", VideoDetailView.as_view(), name="video_detail"),
    path("", VideoListView.as_view(), name="video_list"),

]
