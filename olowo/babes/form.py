from django import forms
from .models import Babes


class MyBabes(forms.ModelForm):
    class Meta:
        model = Babes
        fields = "__all__"
