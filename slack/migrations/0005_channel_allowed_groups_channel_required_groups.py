# Generated by Django 4.2.13 on 2025-01-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("slack", "0004_remove_channel_channel_id_alter_channel_id")
    ]

    operations = [
        migrations.AddField(
            model_name="channel",
            name="allowed_groups",
            field=models.ManyToManyField(
                blank=True,
                related_name="allowed_channels",
                to="auth.group",
                verbose_name="Allowed Groups",
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="required_groups",
            field=models.ManyToManyField(
                blank=True,
                related_name="required_channels",
                to="auth.group",
                verbose_name="Required Groups",
            ),
        ),
    ]
