# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='mobile_no',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
    ]