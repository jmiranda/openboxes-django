# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170306_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit_of_measure',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
