from django import forms
from .models import Devices

class DevicesUpdateForm(forms.ModelForm):
    class Meta:
        model = Devices
        fields = ['last_query']