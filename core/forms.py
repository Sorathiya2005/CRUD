from django import forms
from .models import Student

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name","roll","city")
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'})
        }