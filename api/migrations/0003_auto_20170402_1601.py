# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170402_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='password',
            field=models.CharField(default='password', max_length=100, null=True),
        ),
    ]
