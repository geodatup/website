# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-13 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20161112_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='css_color',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]