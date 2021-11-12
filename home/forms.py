from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Employee, Department


        
class RegisterForm(UserCreationForm):
    ROLE = (
        ("CIO", "Chief Information Officer"),
        ("COO", "Chief Operations Officer"),
        ("GM", "General Manager"),
        ("MO", "Marketing Officer"),
        ("HRM", "Human Resource Manager")
    )
    MARITAL_STATUS = (
        ("Single", "Single"),
        ("Married","Married"),
        ("Divorced", "Divorced"),
        ("Separated", "Separated"),
        ("Widowed", "Widowed"),
    )
    LEVELS = (
        ("MSCE","MSCE"),
        ("Diploma", "Diploma"),
        ("Bsc Degree", "Bsc Degree"),
        ("Masters", "Masters")
    )
    COUNTRIES = (
        ("Malawian","Malawian"),
        ("Kenyan", "Kenyan"),
        ("Zimbawean", "Zimbawean"),
    )
    GENDER = (
        ("Male","Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    dob = forms.DateField()
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS)
    education_level = forms.ChoiceField(choices=LEVELS)
    gender = forms.ChoiceField( choices=GENDER)
    nationality = forms.ChoiceField( choices=COUNTRIES)
    class Meta:
        model = Employee
        fields = '__all__'
