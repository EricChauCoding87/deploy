# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-01 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_auto_20180401_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='added_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='travels', to='first_app.Users'),
        ),
    ]