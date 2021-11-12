from home.models import Employee
from home.forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.  
def sign_up(request):
    context = {}
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,Employee)
            return render(request,'home/home.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)
