# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20161023_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Justificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justi_eje', models.TextField(blank=True, null=True)),
                ('justi_indicador', models.TextField(blank=True, null=True)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]