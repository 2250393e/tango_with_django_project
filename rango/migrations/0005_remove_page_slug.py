# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-07 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20180207_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
