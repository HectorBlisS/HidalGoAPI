# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_auto_20161023_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='anexo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]