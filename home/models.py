# from django.utils import timezone
from django.contrib.auth.models import Group, AbstractUser
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
    COUNTRIES = (
        ("Malawian","Malawian"),
        ("Kenyan", "Kenyan"),
        ("Zimbawean", "Zimbawean"),
    )
    GENDER = (
        ("Male","Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    dob = models.DateField(null=True)
    marital_status = models.CharField(max_length=50,choices=MARITAL_STATUS, default="Single")
    education_level = models.CharField(max_length=120, choices=LEVELS, null=True)
    # username = None
    department = models.ForeignKey('Department', blank=True, null=True,on_delete=models.CASCADE)
    gender = models.CharField(max_length=120, choices=GENDER, null=True)
    nationality = models.CharField(max_length=120, choices=COUNTRIES, null=True)
    manager = models.ForeignKey('self', blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.username
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
    COUNTRIES = (
        ("Malawian","Malawian"),
        ("Kenyan", "Kenyan"),
        ("Zimbawean", "Zimbawean"),
    )
    GENDER = (
        ("Male","Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    dob = models.DateField(null=True, blank=True)
    marital_status = models.CharField(max_length=50,choices=MARITAL_STATUS, default="Single")
    education_level = models.CharField(max_length=120, choices=LEVELS,blank=True, null=True)
    # username = None
    department = models.ForeignKey('Department', blank=True, null=True,on_delete=models.CASCADE)
    sex = models.CharField(max_length=120, choices=GENDER, blank=True, null=True)
    nationality = models.CharField(max_length=120, choices=COUNTRIES, blank=True, null=True)
    manager = models.ForeignKey('self', blank=True, null=True,on_delete=models.CASCADE)

class Department(Group):
    hod = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="department_head", null=True, blank=True)
    members = models.ManyToManyField(Employee, related_name="department_members", blank=True)

    def __str__(self):
        return self.name

class Contractor(models.Model):
    name = models.CharField(max_length=150)
    departments = models.ManyToManyField("Department")

    def __str__(self):
        return self.name

class EmployeeLeave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_start_date = models.DateTimeField(auto_now_add=True)
    leave_taken = models.BooleanField(default=False)  
    leave_end_date = models.DateTimeField()
    leave_end = models.BooleanField(default=False)

    def __str__(self):
        return self.employee.username 


class Meeting(models.Model):
    agenda = models.CharField(max_length=50)
    leader = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="meeting_leader", blank=True)
    briefing = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    files = models.ManyToManyField("MeetingFile", related_name="meeting_Files")
    participants = models.ManyToManyField(Employee)
    notes_taker = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="note_taker", blank=True, null=True)
    

    def __str__(self):
        return self.agenda

class MeetingFile(models.Model):
    file = models.FileField(upload_to="media/", max_length=254, null=True, blank=True)
    date_uploaded = models.DateField(auto_now_add=True)


class Goal(models.Model):
    name = models.CharField(max_length=50)
    accomplished = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    manager = models.ManyToManyField(Employee, blank=True)
    members = models.ManyToManyField(Employee, related_name="project_members")
    goals = models.ManyToManyField(Goal, related_name="project_Goals")
    files = models.ManyToManyField("ProjectFile", related_name="project_Files")
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()

    def __str__(self):
        return self.title

class ProjectFile(models.Model):
    file = models.FileField(upload_to="media/", max_length=254, null=True, blank=True)
    date_uploaded = models.DateField(auto_now_add=True)

class Task(models.Model):
    STATUS=(
        ("Completed", "Completed"),
        ("pending", "pending"),
        ("Not Completed", "Not Completed"),
    )
    title = models.CharField(max_length=50)
    handler = models.OneToOneField("Employee", on_delete=models.CASCADE, related_name="task_handler", blank=True)
    assigned_date = models.DateField(auto_now_add=False, blank=True, null=True)
    completion_date = models.DateField(auto_now_add=False, blank=True, null=True)
    status = models.CharField(max_length=120, choices=STATUS, null=True)
    
    
    def __str__(self):
        return self.title