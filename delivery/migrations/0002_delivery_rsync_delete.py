# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-15 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='rsync_delete',
            field=models.BooleanField(default=True, verbose_name='\u540c\u6b65\u5220\u9664'),
        ),
    ]
