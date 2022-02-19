# Generated by Django 3.1.14 on 2022-02-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20220204_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='event2019',
            name='event_id',
            field=models.IntegerField(blank=True, help_text='The 25Live event ID. If not provided, it will be generated from the reference code.', null=True),
        ),
        migrations.AddField(
            model_name='event2019',
            name='reference_code',
            field=models.CharField(blank=True, help_text='The 25Live reference code, found on the event page', max_length=12, null=True),
        ),
    ]