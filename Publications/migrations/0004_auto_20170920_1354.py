# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publications', '0003_auto_20170916_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='file',
            field=models.FileField(null=True, upload_to='Publications/media/pdfs/'),
        ),
    ]