# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-09 05:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20200803_0208'),
        ('data', '0005_auto_20200327_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('developer', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('api_key', models.CharField(max_length=36, verbose_name=b'API Key')),
                ('enabled', models.BooleanField()),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('endpoints', models.ManyToManyField(blank=True, related_name='apps', to='api.Endpoint')),
                ('users', models.ManyToManyField(blank=True, related_name='connected_services', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Third-party application',
            },
        ),
    ]