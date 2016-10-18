# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20161013_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='css_datacategory',
            field=models.CharField(choices=[('products', 'products'), ('help', 'help'), ('documentation', 'documentation'), ('use-cases', 'use-cases'), ('aucun', '')], max_length=50, default=''),
        ),
    ]
