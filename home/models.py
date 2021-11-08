# from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User, PermissionsMixin, BaseUserManager
# from django.utils.translation import gettext_lazy as _

from django.db import models
from django.db.models import manager
from django.db.models.base import ModelState
from django.db.models.deletion import SET_NULL
from phonenumber_field.modelfields import PhoneNumberField

class Employee(AbstractUser):
    ROLE = (
        ("CIO", "Chief Information Officer"),
        ("COO", "Chief Operations Officer"),
        ("GM", "General Manager"),
        ("MO", "Marketing Officer"),
        ("HRM", "Human Resource Manager")
    )
    MARITAL_STATUS = (
        ("Single", "Single"),
        ("Married","Married"),
        ("Divorced", "Divorced"),
        ("Separated", "Separated"),
        ("Widowed", "Widowed"),
    )
    LEVELS = (
        ("MSCE","MSCE"),
        ("Diploma", "Diploma"),
        ("Bsc Degree", "Bsc Degree"),
        ("Masters", "Masters")
    )
    dob = models.DateField(null=True)
    marital_status = models.CharField(max_length=50,choices=MARITAL_STATUS, default="Single")
    education_level = models.CharField(max_length=120, choices=LEVELS, null=True)
    # username = None
    subsidiary =  models.ForeignKey("Subsidiary", on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey("Department", on_delete=models.CASCADE, blank=True, null=True)
    manager = models.ForeignKey('self', blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Department(models.Model):
    hod = models.ForeignKey("Employee", on_delete=models.CASCADE, related_name="department_head", null=True, blank=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Subsidiary(models.Model):
    name = models.CharField(max_length=50)
    general_manager = models.ForeignKey(Employee, blank=True, null=True,on_delete=models.CASCADE, related_name="general_manager")

    def __str__(self):
        return self.name


class Contractor(models.Model):
    name = models.CharField(max_length=150)
    departments = models.ManyToManyField("Department")

    def __str__(self):
        return self.name

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_taken = models.BooleanField(default=False)  
    leave_end = models.BooleanField(default=False)

    def __str__(self):
        return self.employee.first_name 


class Meeting(models.Model):
    agenda = models.CharField(max_length=50)
    leader = models.OneToOneField("Employee", on_delete=models.CASCADE, related_name="meeting_leader", blank=True)
    briefing = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participants = models.ManyToManyField(Employee)

    def __str__(self):
        return self.agenda

class Goal(models.Model):
    name = models.CharField(max_length=50)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    manager = models.OneToOneField('Employee', blank=True, null=True,on_delete=models.CASCADE)
    members = models.ManyToManyField(Employee, related_name="project_members")
    goals = models.ManyToManyField(Goal, related_name="project_Goals")
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()

    def __str__(self):
        return self.title
