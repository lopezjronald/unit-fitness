from .views import (VideoListView,
                    VideoDetailView,
                    VideoCreateView,
                    VideoUpdateView,
                    VideoDeleteView,
                    SearchResultsListView)
from django.urls import path

app_name = "videos"

urlpatterns = [
    path("<int:pk>/delete/", VideoDeleteView.as_view(), name="video_delete"),
    path("<int:pk>/edit/", VideoUpdateView.as_view(), name="video_edit"),
    path("new/", VideoCreateView.as_view(), name="video_new"),
    path("<int:pk>/", VideoDetailView.as_view(), name="video_detail"),
    path("", VideoListView.as_view(), name="video_list"),

    # Search URL
    path("search/", SearchResultsListView.as_view(), name="search_results"),

]
