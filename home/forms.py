from django.db.models import fields
from django.forms import ModelForm
from .models import Employee, EmployeeInfomation, Department, Project, Meeting, Leave, Contractor

class EmployeeCreationForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['__all__']