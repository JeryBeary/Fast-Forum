# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 22:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20160524_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='replyTo',
        ),
    ]
