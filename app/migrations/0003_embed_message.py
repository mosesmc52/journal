# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_embed'),
    ]

    operations = [
        migrations.AddField(
            model_name='embed',
            name='message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
