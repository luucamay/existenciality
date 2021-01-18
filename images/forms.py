from django import forms
from .models import *


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['photo']
