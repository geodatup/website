# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('website', '0007_section_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_reference', models.CharField(max_length=15)),
                ('pitch', models.CharField(null=True, max_length=30, blank=True)),
                ('css_icon', models.CharField(null=True, max_length=15, blank=True)),
                ('css_class', models.CharField(null=True, max_length=100, blank=True)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, null=True, to='filer.Image', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='css_icon',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='software',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, null=True, to='filer.Image', blank=True),
        ),
    ]
