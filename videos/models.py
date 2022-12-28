from documents.models import Document
from django.db import models
from django.urls import reverse


class Video(models.Model):
    VIDEO_TYPES = [
        ("Training", "Training"),
        ("PT Assessment", "PT Assessment"),
        ("Unit", "Unit"),
        ("Other", "Other"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True, choices=VIDEO_TYPES)
    embedded_url = models.CharField(max_length=500)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("videos:video_detail", kwargs={"pk": self.pk})
