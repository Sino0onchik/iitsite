# Generated by Django 5.0.6 on 2024-06-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_page_pagefile_pageimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagefile',
            name='image',
        ),
        migrations.AddField(
            model_name='pagefile',
            name='file',
            field=models.FileField(default=1, upload_to='files/'),
            preserve_default=False,
        ),
    ]