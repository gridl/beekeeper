# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-21 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0009_add_timeout'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='max_instances',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='min_instances',
            field=models.IntegerField(default=0),
        ),
    ]