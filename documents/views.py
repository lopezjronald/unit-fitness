from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bulletin, Document


# Bulletin Views
class BulletinListView(ListView):
    model = Bulletin
    template_name = "documents/bulletin_list.html"
    context_object_name = "bulletin_list"
    paginate_by = 5


class BulletinDetailView(DetailView):
    model = Bulletin
    template_name = "documents/bulletin_detail.html"


class BulletinUpdateView(UpdateView):
    model = Bulletin
    fields = (
        "start_date",
        "end_date",
        "url",
    )
    template_name = "documents/bulletin_edit.html"


class BulletinCreateView(CreateView):
    model = Bulletin
    template_name = "documents/bulletin_new.html"
    fields = ["start_date", "end_date", "url"]


class BulletinDeleteView(DeleteView):
    model = Bulletin
    template_name = "documents/bulletin_delete.html"
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
