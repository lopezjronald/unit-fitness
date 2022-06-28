from django.db import models
from django.urls import reverse


class Assessment(models.Model):
    time = models.TimeField()
    date = models.DateField()

    class Meta:
        ordering = ["-date", "time"]

    def __str__(self):
        day_name = self.date.strftime('%A')
        day = self.date.strftime('%d')
        month = self.date.strftime('%B')
        year = self.date.strftime('%Y')
        time = self.time.strftime('%H:%M')
        return f"{day_name}, {month} {day}, {year} @ {time}"


    def get_absolute_url(self):
        return reverse("assessment_list")


class Tester(models.Model):
    RANK_CHOICES = [
        ("AB", "AB"),
        ("AMN", "AMN"),
        ("A1C", "A1C"),
        ("SRA", "SRA"),
        ("SSGT", "SSGT"),
        ("TSGT", "TSGT"),
        ("MSGT", "MSGT"),
        ("SMSGT", "SMSGT"),
        ("CMSGT", "CMSGT"),
        ("2LT", "2LT"),
        ("1LT", "1LT"),
        ("CAPT", "CAPT"),
        ("MAJ", "MAJ"),
        ("LT COL", "LT COL"),
        ("COL", "COL"),
        ("BRIG GEN", "BRIG GEN"),
        ("MAJ GEN", "MAJ GEN"),
        ("LT GEN", "LT GEN"),
        ("GEN", "GEN"),
    ]
    rank = models.CharField(max_length=50, choices=RANK_CHOICES, default="AB")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.rank} {self.first_name} {self.last_name}"