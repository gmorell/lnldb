# Generated by Django 3.1.2 on 2020-10-29 02:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import meetings.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Start Time')),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('agenda', models.TextField(blank=True, null=True)),
                ('minutes', models.TextField(blank=True, null=True)),
                ('minutes_private', models.TextField(blank=True, null=True, verbose_name='Closed Minutes')),
                ('attendance', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.location')),
            ],
            options={
                'ordering': ('-datetime',),
                'permissions': (('view_mtg', 'See all meeting info'), ('edit_mtg', 'Edit all meeting info'), ('view_mtg_attendance', 'See meeting attendance'), ('list_mtgs', 'List all meetings'), ('create_mtg', 'Create a meeting'), ('send_mtg_notice', 'Send meeting notices manually'), ('view_mtg_closed', 'See closed meeting info')),
            },
        ),
        migrations.CreateModel(
            name='MeetingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TargetEmailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MtgAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=64)),
                ('file', models.FileField(upload_to=meetings.models.mtg_attachment_file_name)),
                ('private', models.BooleanField(default=False)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('meeting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='meetings.meeting')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeetingAnnounce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=128)),
                ('message', models.TextField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('email_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meetings.targetemaillist')),
                ('events', models.ManyToManyField(blank=True, related_name='meetingannouncements', to='events.BaseEvent')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.meeting')),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='meetings.meetingtype'),
        ),
        migrations.CreateModel(
            name='CCNoticeSend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('sent_success', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('addtl_message', models.TextField(blank=True, null=True, verbose_name='Additional Message')),
                ('email_to', models.ForeignKey(default=meetings.models.get_default_email, on_delete=django.db.models.deletion.PROTECT, to='meetings.targetemaillist')),
                ('events', models.ManyToManyField(blank=True, related_name='meetingccnoticeevents', to='events.BaseEvent')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetingccnotices', to='meetings.meeting')),
            ],
        ),
        migrations.CreateModel(
            name='AnnounceSend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('sent_success', models.BooleanField(default=False)),
                ('announce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.meetingannounce')),
            ],
        ),
    ]
