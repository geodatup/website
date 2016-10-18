# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20161013_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatFormation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nom_categorie', models.CharField(max_length=15)),
                ('pitch', models.CharField(max_length=30, null=True, blank=True)),
                ('css_icon', models.CharField(max_length=15, null=True, blank=True)),
                ('css_class', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='formation',
            name='categorie_service',
        ),
        migrations.AddField(
            model_name='catformation',
            name='formations',
            field=models.ManyToManyField(to='website.Formation', null=True, blank=True),
        ),
    ]
