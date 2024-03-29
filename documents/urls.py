from django.urls import path
from . import views

app_name = "documents"

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

    # Information urls
    path("information/", views.InformationListView.as_view(), name="information_list"),

    # Testing Form urls
    path("testing-forms/", views.TestingFormListView.as_view(), name="testing_form_list"),

    # Document urls
    path("<int:pk>/delete/", views.DocumentDeleteView.as_view(), name="document_delete"),
    path("<int:pk>/edit/", views.DocumentUpdateView.as_view(), name="document_edit"),
    path("<int:pk>/", views.DocumentDetailView.as_view(), name="document_detail"),
    path("new/", views.DocumentCreatView.as_view(), name="document_new"),
    path("", views.DocumentListView.as_view(), name="all_documents"),

    # Search URL
    path("search/", views.SearchResultsListView.as_view(), name="search_results"),

]
