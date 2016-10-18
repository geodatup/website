# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20161005_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nom_formation', models.CharField(max_length=15)),
                ('pitch', models.CharField(max_length=30, null=True, blank=True)),
                ('contenu', models.CharField(max_length=100, null=True, blank=True)),
                ('niveau', models.CharField(max_length=15)),
                ('prerequis', models.CharField(max_length=15)),
                ('duree', models.CharField(max_length=15)),
                ('tarif', models.CharField(max_length=15)),
                ('css_icon', models.CharField(max_length=15, null=True, blank=True)),
                ('css_class', models.CharField(max_length=100, null=True, blank=True)),
                ('categorie_service', models.ForeignKey(to='website.Categorie', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nom_soft', models.CharField(max_length=15)),
                ('pitch', models.CharField(max_length=30, null=True, blank=True)),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
                ('css_icon', models.CharField(max_length=15, null=True, blank=True)),
                ('css_class', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='service',
            old_name='nom_icon',
            new_name='css_icon',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='big_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='short_description',
            new_name='pitch',
        ),
        migrations.AddField(
            model_name='formation',
            name='logiciels',
            field=models.ManyToManyField(to='website.Software', null=True, blank=True),
        ),
    ]
