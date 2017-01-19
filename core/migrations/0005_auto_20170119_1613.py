# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170119_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='code',
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='expiration_date',
            field=models.DateField(null=True),
        ),
    ]
