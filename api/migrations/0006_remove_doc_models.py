# Generated by Django 3.1.8 on 2021-12-10 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_remove_extension_endpoints'),
        ('api', '0005_auto_20200803_0208'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Method',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='Parameter',
        ),
        migrations.DeleteModel(
            name='RequestParameter',
        ),
        migrations.DeleteModel(
            name='ResponseKey',
        ),
        migrations.DeleteModel(
            name='Endpoint',
        ),
    ]
