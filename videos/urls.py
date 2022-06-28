from .views import (VideoListView,
                    VideoDetailView,
                    VideoCreateView,
                    VideoUpdateView,
                    VideoDeleteView)
from django.urls import path

urlpatterns = [
    path("<int:pk>/", VideoDetailView.as_view(), name="video_detail"),
    path("", VideoListView.as_view(), name="video_list"),

]
