# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-21 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('website', '0028_formation_css_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContenuFormation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_contenu', models.CharField(max_length=100)),
                ('acquis', models.CharField(blank=True, max_length=100, null=True)),
                ('actif', models.BooleanField(default=True)),
                ('slug', models.SlugField(default='', help_text='indiquer un nom unique pour url', max_length=64, verbose_name='slug')),
            ],
        ),
        migrations.AddField(
            model_name='catformation',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.Image'),
        ),
        migrations.RemoveField(
            model_name='formation',
            name='contenu',
        ),
        migrations.AlterField(
            model_name='formation',
            name='duree',
            field=models.CharField(choices=[('une demi journée', '1/2/j'), ('une journée', '1j'), ('2 jours', '2j'), ('3 jours', '3j')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='formation',
            name='contenu',
            field=models.ManyToManyField(blank=True, to='website.ContenuFormation'),
        ),
    ]