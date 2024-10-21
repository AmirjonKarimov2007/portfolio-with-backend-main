# Generated by Django 5.0 on 2024-10-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Yosh'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_logos'),
        ),
    ]
