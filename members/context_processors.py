from members.models import PhysicalTrainingLeader, UnitFitnessAssessmentCell, UnitFitnessProgramManager


def physical_training_leader(request):
    ptl_list = PhysicalTrainingLeader.objects.all()
    return {"ptl_list": ptl_list}


def unit_fitness_assessment_cell(request):
    ufac_list = UnitFitnessAssessmentCell.objects.all()
    return {"ufac_list": ufac_list}


def unit_fitness_program_manager(request):
    ufpm_list = UnitFitnessProgramManager.objects.all()
    return {"ufpm_list": ufpm_list}
