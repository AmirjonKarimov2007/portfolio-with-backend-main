# Generated by Django 5.0 on 2024-08-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_projectphotos_remove_project_photo_project_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ManyToManyField(blank=True, null=True, to='portfolio.projectphotos', verbose_name='Rasmlar'),
        ),
    ]
