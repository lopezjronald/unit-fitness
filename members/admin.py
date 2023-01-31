from django.contrib import admin

from .models import (Member,
                     PhysicalTrainingLeader,
                     UnitFitnessProgramManager,
                     UnitFitnessAssessmentCell,
                     Commander,
                     NonCurrentMember,
                     UnsatisfactoryMember,
                     SpecialMember)

admin.site.register(Member)
admin.site.register(Commander)
admin.site.register(NonCurrentMember)
admin.site.register(UnsatisfactoryMember)
admin.site.register(PhysicalTrainingLeader)
admin.site.register(UnitFitnessProgramManager)
admin.site.register(UnitFitnessAssessmentCell)
admin.site.register(SpecialMember)
