# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-15 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0011_auto_20181011_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='devis',
            name='commentaire',
            field=models.TextField(blank=True, null=True),
        ),
    ]