# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20170225_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('url', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='StudentPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=256)),
            ],
        ),
    ]