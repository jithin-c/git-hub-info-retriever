# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-30 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest-api', '0002_auto_20170930_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gituser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]