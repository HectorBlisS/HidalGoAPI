# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20161009_0524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='projects',
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(related_name='projects', to='projects.Category'),
        ),
    ]
