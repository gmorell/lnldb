# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-28 22:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_trainings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='training',
            options={'ordering': ['-date', '-recorded_on'], 'permissions': (('view_training_details', 'View a training'),)},
        ),
    ]