# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-02 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
    ]
