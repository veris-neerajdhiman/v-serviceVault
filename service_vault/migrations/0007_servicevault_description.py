# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_vault', '0006_remove_servicevault_assign_to_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicevault',
            name='description',
            field=models.TextField(blank=True, help_text='Service Description', null=True, verbose_name='Service Description'),
        ),
    ]