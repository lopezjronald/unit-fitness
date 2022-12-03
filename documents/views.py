from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bulletin, Document

from django.db.models import Q  # for query search


# Bulletin Views
class BulletinListView(ListView):
    model = Bulletin
    template_name = "documents/bulletin/bulletin_list.html"
    context_object_name = "bulletin_list"
    paginate_by = 5


class BulletinDetailView(DetailView):
    model = Bulletin
    template_name = "documents/bulletin/bulletin_detail.html"
    context_object_name = "bulletin"


class BulletinCreateView(LoginRequiredMixin, CreateView):
    model = Bulletin
    template_name = "documents/bulletin/bulletin_new.html"
    fields = ["start_date", "end_date", "url", "embedded_url"]


class BulletinUpdateView(LoginRequiredMixin, UpdateView):
    model = Bulletin
    fields = (
        "start_date",
        "end_date",
        "url",
        "embedded_url",
    )
    template_name = "documents/bulletin/bulletin_edit.html"


class BulletinDeleteView(LoginRequiredMixin, DeleteView):
    model = Bulletin
    template_name = "documents/bulletin/bulletin_delete.html"
    success_url = reverse_lazy("bulletin_list")


# Appointment Letter Views
class AppointmentLetterListView(ListView):
    model = Document
    template_name = "documents/appointment-letters/appointment-letter_list.html"
    context_object_name = "appointment_letter_list"


# Google Form Views
class GoogleFormListView(ListView):
    model = Document
    template_name = "documents/forms/google-form_list.html"
    context_object_name = "google_form_list"
    paginate_by = 5


# Testing Form Views
class TestingFormListView(ListView):
    model = Document
    template_name = "documents/forms/testing-form_list.html"
    context_object_name = "testing_form_list"


# Information Views
class InformationListView(ListView):
    model = Document
    template_name = "documents/information/information_list.html"
    context_object_name = "information_list"
    paginate_by = 5


# Document Views
class DocumentListView(ListView):
    model = Document
    template_name = "documents/document_list.html"
    context_object_name = "all_documents"


class DocumentDetailView(DetailView):
    model = Document
    template_name = "documents/document_detail.html"
    context_object_name = "document"


class DocumentCreatView(LoginRequiredMixin, CreateView):
    model = Document
    template_name = "documents/document_new.html"
    fields = ["title", "description", "type", "url", "embedded_url"]
    success_url = reverse_lazy("all_documents")


class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    model = Document
    fields = (
        "title",
        "description",
        "type",
        "url",
        "embedded_url",
    )
    template_name = "documents/document_edit.html"


class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = Document
    template_name = "documents/document_delete.html"
    success_url = reverse_lazy("home")


class SearchResultsListView(ListView):
    template_name = "documents/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Document.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(type__icontains=query)
        ).order_by("title")
