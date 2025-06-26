from django import forms
from .models import Gift_Name





class Gift_Name_Form(forms.ModelForm):
    class Meta:
        model = Gift_Name
        fields = '__all__'
        exclude = ['slug']
