from django.views.generic import TemplateView, ListView
from .models import Faq

class HomePageView(TemplateView):
    template_name = "home.html"


class FaqPageView(ListView):
    model = Faq
    template_name = "faq.html"
    context_object_name = "faq_list"
    paginate_by = 10