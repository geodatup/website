# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-21 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20161021_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='catformation',
            name='css_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='secteur',
            name='css_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='secteur',
            name='css_icon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]