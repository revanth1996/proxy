# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.IntegerField(default=2017),
        ),
    ]
