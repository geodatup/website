# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='categorie_service',
        ),
        migrations.AddField(
            model_name='categorie',
            name='service_categorie',
            field=models.ForeignKey(to='website.Service', null=True, blank=True),
        ),
    ]
