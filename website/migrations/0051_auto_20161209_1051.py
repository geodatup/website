# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-09 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0050_auto_20161122_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='unité',
            new_name='unite',
        ),
    ]
