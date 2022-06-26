from django.contrib import admin
from .models import Assessment, Tester


class TesterInline(admin.TabularInline):
    model = Tester
    extra = 0
    verbose_name = "Airman"
    verbose_name_plural = "Airmen"


class AssessmentAdmin(admin.ModelAdmin):
    inlines = [
        TesterInline,
    ]
    list_display = ("date", "time")


admin.site.register(Assessment, AssessmentAdmin)
