# Generated by Django 5.0 on 2024-09-20 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('defaults', '0003_homedefault_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='static',
            name='resume',
        ),
    ]
