from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Video

from django.db.models import Q  # for query search


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
    success_url = reverse_lazy("videos:video_list")


class SearchResultsListView(ListView):
    model = Video
    context_object_name = "video_list"
    template_name = "videos/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Video.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(type__icontains=query)
        ).order_by("title")
