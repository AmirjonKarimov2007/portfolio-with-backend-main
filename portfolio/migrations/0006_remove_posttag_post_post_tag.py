# Generated by Django 5.0 on 2024-09-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_posttag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posttag',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='portfolio.posttag'),
        ),
    ]