# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-11 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20161028_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='level',
            field=models.PositiveSmallIntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]