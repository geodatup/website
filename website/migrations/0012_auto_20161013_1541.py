# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_section_css_datacategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='css_datacategory',
            field=models.CharField(choices=[('products', 'products'), ('help', 'help'), ('documentation', 'documentation'), ('use-cases', 'use-cases'), ('', 'aucun')], max_length=50, default=''),
        ),
    ]
