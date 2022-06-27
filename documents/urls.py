from django.urls import path
from .views import BulletinListView, BulletinDetailView, BulletinUpdateView, BulletinCreateView, BulletinDeleteView

urlpatterns = [

    # urls for bulletin model
    path("bulletin/<int:pk>/delete/", BulletinDeleteView.as_view(), name="bulletin_delete"),
    path("bulletin/<int:pk>/edit/", BulletinUpdateView.as_view(), name="bulletin_edit"),
    path("bulletin/new/", BulletinCreateView.as_view(), name="bulletin_new"),
    path("bulletin/<int:pk>/", BulletinDetailView.as_view(), name="bulletin_detail"),
    path("bulletin/", BulletinListView.as_view(), name="bulletin_list"),
]
