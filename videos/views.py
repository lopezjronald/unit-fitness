from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Video


class VideoListView(ListView):
    model = Video
    template_name = "videos/video_list.html"
    context_object_name = "video_list"
    paginate_by = 5


class VideoDetailView(DetailView):
    model = Video
    template_name = "videos/video_detail.html"
    context_object_name = "video"


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    template_name = "videos/video_new.html"
    fields = [
        "title",
        "description",
        "type",
        "embedded_url",
    ]


class VideoUpdateView(LoginRequiredMixin, UpdateView):
    model = Video
    fields = (
        "title",
        "description",
        "type",
        "embedded_url",
    )
    template_name = "videos/video_edit.html"


class VideoDeleteView(LoginRequiredMixin, DeleteView):
    model = Video
    template_name = "videos/video_delete.html"
    success_url = reverse_lazy("video_list")
