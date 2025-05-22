from django import forms
from application1.models import addhod

class addhodFORM(forms.ModelForm):
    class Meta:
        model = addhod
        fields='__all__'

