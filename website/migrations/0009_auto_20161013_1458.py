# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20161013_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='secteur',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='section',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='service',
            name='actif',
            field=models.BooleanField(default=True),
        ),
    ]
