# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-29 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0010_auto_20170929_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='guest',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
