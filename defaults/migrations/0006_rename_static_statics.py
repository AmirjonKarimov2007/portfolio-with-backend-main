# Generated by Django 5.0 on 2024-09-20 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('defaults', '0005_remove_static_static'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Static',
            new_name='Statics',
        ),
    ]
