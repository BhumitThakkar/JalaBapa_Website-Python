# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About_Us', '0002_auto_20170914_1033'),
        ('Activities', '0003_auto_20170921_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='contact_persons',
        ),
        migrations.AddField(
            model_name='activities',
            name='contact_persons',
            field=models.ManyToManyField(to='About_Us.Authorized_Members'),
        ),
    ]