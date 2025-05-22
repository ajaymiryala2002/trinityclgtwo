from django import forms
from application1.models import FEES

class FEESFORMS(forms.ModelForm):
    class Meta:
        model = FEES
        fields = '__all__'