# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20161013_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='nom_categorie',
            field=models.CharField(max_length=30),
        ),
    ]
