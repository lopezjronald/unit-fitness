from rest_framework.generics import ListAPIView

from members.models import Member
from .serializers import MemberSerializer


class MemberAPIView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

