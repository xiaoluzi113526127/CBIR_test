# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CBIR', '0004_cbirs_1024_feature_cbirs_64_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbirs_64_feature',
            name='tag',
            field=models.CharField(default='a', max_length=20),
        ),
    ]