# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-01 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_travel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='travel_date_from',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='travel_date_to',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
