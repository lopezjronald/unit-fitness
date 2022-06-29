from django import forms

from .models import Tester


class TesterForm(forms.ModelForm):
    class Meta:
        model = Tester
        fields = ("rank", "first_name", "last_name")
