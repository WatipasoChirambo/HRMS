from django.contrib import admin
from .models import Employee,EmployeeLeave, Department, Contractor, Meeting, Project, Goal, ProjectFile, Task, MeetingFile
from django.contrib.auth.admin import UserAdmin
from home.forms import RegisterForm, CustomUserChangeForm
from home.models import Employee
# Register your models here
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Meeting)
admin.site.register(Contractor)
admin.site.register(Goal)
admin.site.register(ProjectFile)
admin.site.register(EmployeeLeave)
admin.site.register(Task)
admin.site.register(MeetingFile)

class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = CustomUserChangeForm
    model = Employee

admin.site.register(Employee, CustomUserAdmin)