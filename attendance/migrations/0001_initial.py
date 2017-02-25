# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseID', models.CharField(default='', max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('studentID', models.CharField(default='', max_length=100)),
                ('present', models.BooleanField(default=False)),
                ('year', models.IntegerField(default=2017)),
            ],
        ),
    ]
