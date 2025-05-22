from django import  forms
from application1.models import students
class studentsFORMS(forms.ModelForm):
    class Meta:
        model = students
        fields = '__all__'