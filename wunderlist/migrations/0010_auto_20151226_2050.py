# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wunderlist', '0009_connection_webhook_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='webhook_id',
            field=models.IntegerField(blank=True, default=-1, verbose_name='Webhook ID'),
        ),
    ]
