# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-16 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(1, 'Lowest'), (2, 'Low'), (3, 'Normal'), (4, 'High'), (5, 'Highest')], null=True),
        ),
    ]