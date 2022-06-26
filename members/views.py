from django.views.generic import ListView, DetailView
from .models import Member


class MemberListView(ListView):
    model = Member
    template_name = "members/member_list.html"
    context_object_name = "member_list"


class MemberDetailView(DetailView):
    model = Member
    template_name = "members/member_detail.html"
    context_object_name = "member"
