# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20161013_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catformation',
            name='formations',
            field=models.ManyToManyField(blank=True, to='website.Formation'),
        ),
        migrations.AlterField(
            model_name='formation',
            name='logiciels',
            field=models.ManyToManyField(blank=True, to='website.Software'),
        ),
    ]
