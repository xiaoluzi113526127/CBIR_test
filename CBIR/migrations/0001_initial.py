# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CBIR_IMAGE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(default='a', max_length=20)),
                ('local', models.CharField(default='a', max_length=200)),
            ],
        ),
    ]
