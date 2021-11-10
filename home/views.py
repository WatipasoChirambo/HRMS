from django.shortcuts import render
from .models import Meeting, Project, Department, Employee, Task

# Create your views here.
def index(request):
    staff = Employee.objects.all()
    tasks = Task.objects.all()
    context = {
        'staff':staff,
        "tasks":tasks
    }
    return render(request, 'home/home.html', context)


def meetings_view(request):
    meetings = Meeting.objects.all()
    context = {
        'meetings':meetings
    }
    return render(request, 'home/meetings.html', context)

def departments_view(request):
    departments = Department.objects.all()
    context = {
        'departments':departments,
    }
    return render(request, 'home/departments.html', context)

def staff_view(request):
    staff = Employee.objects.all()
    context = {
        'staff':staff,
    }
    return render(request, 'home/staff.html', context)

def projects_view(request):
    projects = Project.objects.all()
    context = {
        'projects':projects,
    }
    return render(request, 'home/projects.html', context)



