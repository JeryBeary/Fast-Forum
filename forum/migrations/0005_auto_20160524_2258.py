# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 03:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20160524_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='replyTo',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='thread',
        ),
    ]
