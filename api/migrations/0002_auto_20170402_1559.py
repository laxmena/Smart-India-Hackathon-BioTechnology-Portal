# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingprogram',
            name='category',
            field=models.CharField(default='production', max_length=100, null=True),
        ),
    ]