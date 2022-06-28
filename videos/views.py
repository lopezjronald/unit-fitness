from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Video


class VideoListView(ListView):
    model = Video
    template_name = "videos/video_list.html"
    context_object_name = "video_list"
    paginate_by = 10


class VideoDetailView(DetailView):
    model = Video
    template_name = "videos/video_detail.html"
    context_object_name = "video"


class VideoCreateView(CreateView):
    model = Video


class VideoUpdateView(UpdateView):
    model = Video


class VideoDeleteView(DeleteView):
    model = Video

