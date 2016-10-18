# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20161013_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='level',
            field=models.CharField(default='indéfini', max_length=50, choices=[('navbar-top', 'navbar-top'), ('navbar-top-sub1', 'navbar-top-sub1'), ('navbar-top-sub2', 'navbar-top-sub2'), ('navbar-verticale', 'navbar-verticale')]),
        ),
    ]
