# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-29 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0012_auto_20170929_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='end_date',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='end_time',
            field=models.TimeField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='instructor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_date',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_time',
            field=models.TimeField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='summary',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='events',
            name='venue',
            field=models.TextField(max_length=500),
        ),
    ]