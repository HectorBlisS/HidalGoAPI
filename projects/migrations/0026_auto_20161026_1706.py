# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20161026_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='autor_correo',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='autor_name',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='autor_tel',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
