from django import forms
from application1.models import details

class detailsFORMS(forms.ModelForm):
    class Meta:
        model= details
        fields = '__all__'