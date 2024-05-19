# Generated by Django 5.0.6 on 2024-05-19 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_category_alter_cafedra_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='all_news', to='mysite.category'),
        ),
    ]