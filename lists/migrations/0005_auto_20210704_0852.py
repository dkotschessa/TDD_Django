# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-04 08:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_list_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='List',
        ),
        migrations.RemoveField(
            model_name='item',
            name='text',
        ),
    ]
