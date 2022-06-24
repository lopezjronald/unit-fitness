from django.contrib import admin
from .models import Assessment
from members.models import Member


class MemberInline(admin.TabularInline):
    model = Member
    extra = 0
    verbose_name = "Airman"
    verbose_name_plural = "Airmen"


class AssessmentAdmin(admin.ModelAdmin):
    inlines = [
        MemberInline,
    ]
    list_display = ("date", "time")


admin.site.register(Assessment, AssessmentAdmin)
