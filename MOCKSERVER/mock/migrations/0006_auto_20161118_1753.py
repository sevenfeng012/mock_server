# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mock', '0005_auto_20161118_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='content',
            field=models.TextField(help_text='api json data format!'),
        ),
    ]