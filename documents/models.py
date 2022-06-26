from django.db import models


class Document(models.Model):
    DOCUMENT_TYPES = [
        ("Appointment Letter", "Appointment Letter"),
        ("Google Form", "Google Form"),
        ("Information", "Information"),
        ("PT Form", "PT Form"),
    ]
    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.URLField()
    document_created = models.DateTimeField(auto_now_add=True)
    document_updated = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=50, choices=DOCUMENT_TYPES, blank=True, null=True)
    embedded_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
