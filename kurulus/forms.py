from .models import Kurulus
from django import forms

class kurulusForm(forms.ModelForm):

    class Meta:
        model = Kurulus
        fields = "__all__"

