# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-15 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_service_html_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='html_page',
            field=models.CharField(blank=True, default='<p></p>', max_length=10000, null=True),
        ),
    ]
