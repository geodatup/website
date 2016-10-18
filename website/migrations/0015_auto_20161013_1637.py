# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20161013_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='nom_section',
            field=models.CharField(max_length=30),
        ),
    ]
