# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-20 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_auto_20161020_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catformation',
            name='css_icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
