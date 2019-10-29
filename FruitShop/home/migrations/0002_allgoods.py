# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-10-12 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=10)),
                ('productimg', models.CharField(max_length=150)),
                ('productname', models.CharField(max_length=200)),
                ('isxf', models.NullBooleanField(default=False)),
                ('specifics', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=10)),
                ('categoryid', models.CharField(max_length=10)),
                ('childcid', models.CharField(max_length=10)),
                ('dealerid', models.CharField(max_length=10)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'fruit_allgoods',
            },
        ),
    ]