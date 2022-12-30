from .forms import ExemptionForm
from django.views.generic import FormView
from django.urls import reverse_lazy


class ExemptionFormView(FormView):
    form_class = ExemptionForm
    template_name = "memos/exemption.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
