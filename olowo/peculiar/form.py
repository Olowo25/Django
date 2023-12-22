from django import forms
from .models import Details


class MyForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = "__all__"
