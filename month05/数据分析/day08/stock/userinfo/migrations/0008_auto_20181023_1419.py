# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 06:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0007_auto_20181023_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fund',
            old_name='frozenmoney',
            new_name='frozen_money',
        ),
    ]
