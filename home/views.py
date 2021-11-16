from django.http.response import Http404
from django.shortcuts import render, redirect
from .models import Meeting, Project, Department, Employee, Task
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
def index(request):
    staff = Employee.objects.all()
    tasks = Task.objects.all()
    meetings = Meeting.objects.all()
    context = {
        'staff':staff,
        "tasks":tasks,
        "meetings":meetings
    }
    return render(request, 'home/home.html', context)

def add_employee(request):
    context = {}
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            login(request,Employee)
            return render(request,'home/home.html')
    context['form']=form
    return render(request,'registration/register.html',context)
    
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

def department(request, pk):
    try:
        group = Department.objects.get(id=pk)
        members = group.user_set.all()
    except Department.DoesNotExist:
        Http404
    return render(request, 'home/department.html', {"department":members})

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



