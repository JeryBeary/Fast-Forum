# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 04:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20160524_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replyTo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='forum.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='forum.Thread'),
        ),
    ]
