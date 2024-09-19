# Generated by Django 5.0 on 2024-08-22 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_projecttext_project_description_project_project_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='footer_text',
            field=models.TextField(default='', verbose_name='Pastdagi Text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='footer_title',
            field=models.CharField(default='', max_length=200, verbose_name='Pastdagi Sarlavha'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projecttext',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons/'),
        ),
        migrations.AlterField(
            model_name='projecttext',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projecttext',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
