# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-27 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='en_pwd',
            field=models.UUIDField(),
        ),
    ]