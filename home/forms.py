from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Employee
from home.models import Department


        
class RegisterForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['staff_user']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Employee
        fields = UserChangeForm.Meta.fields