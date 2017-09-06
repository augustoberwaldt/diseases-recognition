# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('type', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
