# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-05-28 03:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream_gauge', '0002_jason3_gdr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jason3',
            old_name='gdr',
            new_name='gpn',
        ),
    ]
