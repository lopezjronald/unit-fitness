from django.db import models
from django.urls import reverse

from assessments.models import Assessment


class Member(models.Model):
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
    rank = models.CharField(max_length=10, choices=RANK_CHOICES, default="AB")
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="Phone #")
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("assessment_list")

    class Meta:
        verbose_name = "Airman"
        verbose_name_plural = "Airmen"


class PhysicalTrainingLeader(Member):
    cpr_card = models.URLField(verbose_name="CPR Card URL", )
    ptl_completion_date = models.DateField(blank=True,
                                           null=True,
                                           verbose_name="PTL Completion Date", )
    appointment_letter = models.URLField(verbose_name="Appointment Letter URL")
    cpr_expiration_date = models.DateField(blank=True, null=True, verbose_name="CPR Expiration Date")

    class Meta:
        verbose_name = "PTL"
        verbose_name_plural = "Physical Training Leader Team"
        ordering = ["cpr_expiration_date", "last_name"]

    def __str__(self):
        return f"{self.rank} {self.last_name}, {self.first_name}"

    def get_absolute_url(self):
        return reverse("ptl_list")


class UnitFitnessProgramManager(Member):
    ufpm_completion_date = models.DateField(blank=True,
                                            null=True,
                                            verbose_name="UFPM Completion Date", )
    appointment_letter = models.URLField(verbose_name="Appointment Letter URL")
    written_order = models.URLField(verbose_name="MyFitness Written Order URL", )

    class Meta:
        verbose_name = "UFPM"
        verbose_name_plural = "Unit Fitness Program Manager Team"

    def __str__(self):
        return f"{self.rank} {self.last_name}, {self.first_name}"

    def get_absolute_url(self):
        return reverse("ufpm_list")


class UnitFitnessAssessmentCell(models.Model):
    physical_training_leader = models.ForeignKey(
        PhysicalTrainingLeader,
        on_delete=models.CASCADE,
        verbose_name="PTL",
    )
    ufac_completion_date = models.DateField(blank=True,
                                            null=True,
                                            verbose_name="UFAC Completion Date")
    system_authorization_request = models.URLField(verbose_name="DD Form 2875 - System Authorization Request URL", )
    written_order = models.URLField(verbose_name="MyFitness Written Order URL", )
    user_agreement = models.URLField(verbose_name="MyFitness User Agreement URL")

    class Meta:
        verbose_name = "Unit Fitness Assessment Cell"
        verbose_name_plural = "Unit Fitness Assessment Cell Team"

    def __str__(self):
        return f"{self.physical_training_leader}"

    def get_absolute_url(self):
        return reverse("ufac_list")


class Commander(models.Model):
    commander = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.commander}"


class UnsatisfactoryMember(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        verbose_name="Unsatisfactory Member",
    )
    failure_date = models.DateField()
    retest_date = models.DateField()

    def __str__(self):
        return f"{self.member}"


class NonCurrentMember(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        verbose_name="Non-Current Member",
    )
    test_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.member}"


class SpecialMember(Member):
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("last_name", "first_name",)

    class Meta:
        verbose_name = "Special Member"
        verbose_name_plural = "Special Members"

    def __str__(self):
        return f"{self.rank} {self.last_name}, {self.first_name} {self.middle_name}"