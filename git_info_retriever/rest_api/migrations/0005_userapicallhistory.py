# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-30 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_auto_20170930_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAPICallHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_data', models.CharField(max_length=1500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
