from django import forms
from .models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['name', 'profession', 'area', 'city', 'state']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your profession'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your area'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state'}),
        } 