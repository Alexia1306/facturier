# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-02 10:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0005_auto_20181002_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture',
            name='price',
        ),
    ]