from  django.urls import path
from .views import  index, meetings_view, departments_view, staff_view, projects_view, department, add_employee

urlpatterns = [
    path('' , index, name="home"),
    path("meetings/", meetings_view, name="meetings"),
    path("departments/", departments_view, name="departments"),
    path("department/<int:pk>", department, name="department"),
    path("staff/", staff_view, name="staff"),
    path("projects/", projects_view, name="projects"),
    path("register/", add_employee, name="register"),
]
