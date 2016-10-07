# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20161005_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='service_categorie',
        ),
        migrations.AddField(
            model_name='service',
            name='categorie_service',
            field=models.ForeignKey(blank=True, to='website.Categorie', null=True),
        ),
    ]
