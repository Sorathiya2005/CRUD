from dataclasses import field
from django import forms
from .models import Student

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        field = ("name","roll","city")