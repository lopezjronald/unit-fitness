from django.db import models
from django.urls import reverse


class Faq(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField()
    dafman_documentation = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("faqs")