from django.contrib import admin
from .models import Employee, Department, Contractor, Leave, Meeting, Project, Goal
# Register your models here
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Meeting)
admin.site.register(Contractor)
admin.site.register(Leave)
admin.site.register(Goal)