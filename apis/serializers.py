from rest_framework import serializers

from members.models import Member, UnitFitnessProgramManager, UnitFitnessAssessmentCell, PhysicalTrainingLeader
from assessments.models import Assessment


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            "rank",
            "first_name",
            "middle_name",
            "last_name",
            "phone_number",
            "email",
        )
