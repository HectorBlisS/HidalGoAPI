# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_auto_20161026_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='agree',
            field=models.BooleanField(default=True),
        ),
    ]