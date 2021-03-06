# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-02 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('SIREN', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=50)),
                ('siren', models.IntegerField()),
                ('worker', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('first_name', 'last_name', 'worker', 'siren'),
            },
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('id_Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facture.Client')),
                ('id_Employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facture.Employer')),
            ],
            options={
                'ordering': ('id_Client', 'id_Produit', 'price'),
            },
        ),
        migrations.CreateModel(
            name='Ligne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('reference', models.CharField(max_length=14)),
                ('price', models.IntegerField()),
                ('id_Employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facture.Employer')),
            ],
            options={
                'ordering': ('name', 'description', 'price'),
            },
        ),
        migrations.AddField(
            model_name='ligne',
            name='id_Produit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facture.Produit'),
        ),
        migrations.AddField(
            model_name='facture',
            name='id_Produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facture.Produit'),
        ),
        migrations.AddField(
            model_name='employer',
            name='id_Produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facture.Produit'),
        ),
    ]
