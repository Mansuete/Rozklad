# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-23 06:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPanel', '0003_auto_20171023_0913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessoninday',
            options={'verbose_name': 'Номер урока в навчальний день в деякому класі', 'verbose_name_plural': 'Номери уроків в навчальні дні в деяктих класах'},
        ),
    ]
