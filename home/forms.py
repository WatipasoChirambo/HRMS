from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('username', 'first_name', 'last_name')
