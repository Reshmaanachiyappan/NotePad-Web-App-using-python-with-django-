from django import forms
from .models import NotePadApp


class NotePadAppForm(forms.ModelForm):
    class Meta:
        model = NotePadApp
        fields = "__all__"