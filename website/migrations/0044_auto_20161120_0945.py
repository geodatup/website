# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-20 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0043_auto_20161120_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='produits_lié',
            new_name='produit_lié',
        ),
    ]
