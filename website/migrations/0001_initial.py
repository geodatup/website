# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_categorie', models.CharField(max_length=15)),
                ('css_class', models.CharField(max_length=100, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Secteur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_secteur', models.CharField(max_length=15)),
                ('css_class', models.CharField(max_length=100, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_section', models.CharField(max_length=15)),
                ('css_class', models.CharField(max_length=100, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_service', models.CharField(max_length=15)),
                ('nom_icon', models.CharField(max_length=15, blank=True, null=True)),
                ('short_description', models.CharField(max_length=30, blank=True, null=True)),
                ('big_description', models.CharField(max_length=100, blank=True, null=True)),
                ('css_class', models.CharField(max_length=100, blank=True, null=True)),
                ('categorie_service', models.ForeignKey(to='website.Categorie')),
            ],
        ),
    ]
