# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-10-09 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'fruit_nav',
            },
        ),
        migrations.CreateModel(
            name='SeaFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'seafood',
            },
        ),
        migrations.CreateModel(
            name='Seasonal_Fruits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'fruit_seasonal',
            },
        ),
        migrations.CreateModel(
            name='VC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'fruit_vc',
            },
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'fruit_wheel',
            },
        ),
    ]
