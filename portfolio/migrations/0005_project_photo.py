# Generated by Django 5.0.8 on 2024-08-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_rename_project_name_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
