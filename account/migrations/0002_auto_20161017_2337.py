# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 04:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='udi',
            new_name='uid',
        ),
    ]