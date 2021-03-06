from django.db import models
from django.urls import reverse


class Document(models.Model):
    DOCUMENT_TYPES = [
        ("Appointment Letter", "Appointment Letter"),
        ("Google Form", "Google Form"),
        ("Information", "Information"),
        ("Testing Form", "Testing Form"),
    ]
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=DOCUMENT_TYPES, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    embedded_url = models.CharField(max_length=1000, blank=True, null=True)
    document_created = models.DateTimeField(auto_now_add=True)
    document_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("document_detail", kwargs={"pk": self.pk})


class Bulletin(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    url = models.URLField()
    embedded_url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ("-start_date",)

    def __str__(self):
        # This string returns a formatted date: month name and year, Ex: June 2022
        return f"{self.start_date.strftime('%B')} {self.start_date.strftime('%Y')}"

    def get_absolute_url(self):
        return reverse("bulletin_list")
