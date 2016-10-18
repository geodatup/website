# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20161013_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='css_class',
            new_name='css_ahref_class',
        ),
        migrations.AddField(
            model_name='section',
            name='css_div_class',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
