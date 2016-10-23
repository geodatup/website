# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-19 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20161013_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default='', help_text='indiquer un nom unique pour url', max_length=64, verbose_name='slug'),
        ),
    ]