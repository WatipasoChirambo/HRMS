# Generated by Django 3.2.8 on 2021-11-11 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='notes_taker',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_taker', to=settings.AUTH_USER_MODEL),
        ),
    ]