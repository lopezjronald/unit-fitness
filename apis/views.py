from rest_framework.generics import ListAPIView
from django.contrib.auth.mixins import LoginRequiredMixin

from members.models import Member
from .serializers import MemberSerializer


class MemberAPIView(LoginRequiredMixin, ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

