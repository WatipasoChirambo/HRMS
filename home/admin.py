from django.contrib import admin
from .models import Employee,EmployeeLeave, Department, Contractor, Meeting, Project, Goal, ProjectFile, Task, MeetingFile
# Register your models here
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Meeting)
admin.site.register(Contractor)
admin.site.register(Goal)
admin.site.register(ProjectFile)
admin.site.register(EmployeeLeave)
admin.site.register(Task)
admin.site.register(MeetingFile)