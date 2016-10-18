# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20161013_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='nom_service',
            field=models.CharField(max_length=30),
        ),
    ]
