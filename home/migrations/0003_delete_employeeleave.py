# Generated by Django 3.2.8 on 2021-11-10 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_leave_employeeleave'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmployeeLeave',
        ),
    ]
