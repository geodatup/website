# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20161013_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='categorie',
            name='level',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
