# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 21:43
from __future__ import unicode_literals

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_enable_trigram_extension'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_search_vector',
            field=django.contrib.postgres.search.SearchVectorField(blank=True, null=True),
        ),
    ]
