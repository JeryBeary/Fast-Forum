# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 03:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20160524_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='replies',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='comments',
        ),
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
