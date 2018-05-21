# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0004_auto_20170926_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='status',
            field=models.CharField(choices=[('Past', 'Past'), ('Current', 'Current'), ('Upcoming', 'Upcoming')], max_length=10),
        ),
    ]
