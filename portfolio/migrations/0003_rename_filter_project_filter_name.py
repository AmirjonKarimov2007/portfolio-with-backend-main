# Generated by Django 5.0 on 2024-09-25 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_post_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='filter',
            new_name='filter_name',
        ),
    ]