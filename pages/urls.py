from .views import HomePageView, FaqPageView
from django.urls import path

urlpatterns = [
    path("faq/", FaqPageView.as_view(), name="faq"),
    path("", HomePageView.as_view(), name="home"),
]
