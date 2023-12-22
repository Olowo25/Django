from django import forms
from .models import Album
from .models import Song


class Albumss(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"


class Songss(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"
