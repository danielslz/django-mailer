# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-18 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0005_messagelog_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagelog',
            name='to_addresses',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
