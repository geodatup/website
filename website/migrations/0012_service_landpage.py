# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-14 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20161114_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='landpage',
            field=models.BooleanField(default=True),
        ),
    ]