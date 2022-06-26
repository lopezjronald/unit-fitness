from documents.models import Document
from django.db import models


class Video(models.Model):
    VIDEO_TYPES = [
        ("Training", "Training"),
        ("PT Assessment", "PT Assessment"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=VIDEO_TYPES)
    embedded_url = models.URLField()

    def __str__(self):
        return self.title
