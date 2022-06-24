from django.db import models


class Assessment(models.Model):
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.date
