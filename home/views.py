from django.shortcuts import render
from .models import Meeting, Project

# Create your views here.
def index(request):
    meetings = Meeting.objects.count()
    projects = Project.objects.count()
    context = {
        'meetings':meetings,
        "projects":projects
    }
    return render(request, 'home/home.html', context)


