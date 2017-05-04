# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(max_length=30)),
                ('station_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RainData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddate', models.DateField()),
                ('prcp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rain.Rain')),
            ],
        ),
    ]
