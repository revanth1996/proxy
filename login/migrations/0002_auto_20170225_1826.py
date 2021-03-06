# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='ID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='users',
            name='deptID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
