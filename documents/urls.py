from django.urls import path
from . import views

urlpatterns = [

    # urls for bulletin model
    path("bulletin/<int:pk>/delete/", views.BulletinDeleteView.as_view(), name="bulletin_delete"),
    path("bulletin/<int:pk>/edit/", views.BulletinUpdateView.as_view(), name="bulletin_edit"),
    path("bulletin/new/", views.BulletinCreateView.as_view(), name="bulletin_new"),
    path("bulletin/<int:pk>/", views.BulletinDetailView.as_view(), name="bulletin_detail"),
    path("bulletin/", views.BulletinListView.as_view(), name="bulletin_list"),

    # Appointment Letter urls
    path("appointment-letters/", views.AppointmentLetterListView.as_view(), name="appointment_letter_list"),

    # Google Form urls
    path("google-forms/", views.GoogleFormListView.as_view(), name="google_form_list"),

]
