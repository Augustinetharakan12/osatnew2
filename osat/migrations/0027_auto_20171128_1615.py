# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-28 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osat', '0026_auto_20171128_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='yearout',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
