# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-02 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='req_deg',
            field=models.CharField(default=None, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='req_major',
            field=models.CharField(default=None, max_length=12),
            preserve_default=False,
        ),
    ]
