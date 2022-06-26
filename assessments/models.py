from django.db import models


class Assessment(models.Model):
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return f"{self.date}"


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
