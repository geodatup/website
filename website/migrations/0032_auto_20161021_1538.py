# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-21 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_auto_20161021_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='nom_formation',
            field=models.CharField(max_length=50),
        ),
    ]
