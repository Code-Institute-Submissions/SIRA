from django import forms
from .models import HappyEnding


class HappyEndingForm(forms.ModelForm):
    class Meta:
        model = HappyEnding
        fields = ['name', 'status', 'adoption_date', 'adoption_image',]
        widgets =  {
            'name' : forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. Buddy', 'required': True}),
            'status' : forms.NullBooleanSelect(attrs={'class': 'input' }),
            'adoption_date' : forms.TextInput(attrs={'class': 'input', 'placeholder': 'Day of the adoption e.g. 20 January 2020', 'required': True}),
        }           