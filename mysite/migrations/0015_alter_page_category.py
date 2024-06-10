# Generated by Django 5.0.6 on 2024-06-10 04:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_categorypage_page_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pages', to='mysite.categorypage', verbose_name='категория'),
        ),
    ]
