# Generated by Django 3.2.8 on 2021-11-10 15:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211110_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='department_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
