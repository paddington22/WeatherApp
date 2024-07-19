from django import forms
from .models import Device

class DevicesUpdateForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['last_query']