# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caesar', '0002_auto_20180417_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='brainmodule',
            name='module',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]