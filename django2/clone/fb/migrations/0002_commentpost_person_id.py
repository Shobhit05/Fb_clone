# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-30 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentpost',
            name='person_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]