# Generated by Django 5.0 on 2024-09-25 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='tag nomi')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='portfolio.post')),
            ],
        ),
    ]
