from django.contrib import admin

from .models import Member, PhysicalTrainingLeader, UnitFitnessProgramManager, UnitFitnessAssessmentCell

admin.site.register(Member)
admin.site.register(PhysicalTrainingLeader)
admin.site.register(UnitFitnessProgramManager)
admin.site.register(UnitFitnessAssessmentCell)
