# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_project_alcance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
