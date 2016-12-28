# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='favorite_programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programId', models.CharField(max_length=123)),
                ('name', models.CharField(max_length=123)),
                ('imgPath', models.CharField(max_length=123)),
                ('producer', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='FeedAudioAttach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=123)),
                ('liveUrl', models.CharField(max_length=123)),
                ('img', models.CharField(max_length=123)),
                ('duration', models.CharField(max_length=123)),
                ('phId', models.CharField(max_length=123)),
                ('count', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='FeedHotTopicResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=123)),
                ('createTime', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='FeedTopicAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=123)),
                ('userName', models.CharField(max_length=123)),
                ('avatar', models.CharField(max_length=123)),
                ('intro', models.CharField(max_length=123)),
                ('utPath', models.CharField(max_length=123)),
                ('rankImg', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='FeedTopicShareInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aac', models.CharField(max_length=123)),
                ('link', models.CharField(max_length=123)),
                ('title', models.CharField(max_length=123)),
                ('friendTitle', models.CharField(max_length=123)),
                ('content', models.CharField(max_length=123)),
                ('img', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='FeedTopicSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=123)),
                ('viewCount', models.CharField(max_length=123)),
                ('replyCount', models.CharField(max_length=123)),
                ('threadImg', models.CharField(max_length=123)),
                ('topicId', models.CharField(max_length=123)),
                ('subType', models.CharField(max_length=123)),
                ('subject', models.CharField(max_length=123)),
                ('postTime', models.CharField(max_length=123)),
                ('replyTime', models.CharField(max_length=123)),
                ('topicTag', models.CharField(max_length=123)),
                ('programName', models.CharField(max_length=123)),
                ('programImg', models.CharField(max_length=123)),
                ('producer', models.CharField(max_length=123)),
                ('presenter', models.CharField(max_length=123)),
                ('topicType', models.CharField(max_length=123)),
                ('programId', models.CharField(max_length=123)),
                ('audioAttachList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mock.FeedAudioAttach')),
                ('shareInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mock.FeedTopicShareInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mock.FeedTopicAuthor')),
            ],
        ),
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicId', models.CharField(max_length=123)),
                ('subject', models.CharField(max_length=123)),
                ('content', models.CharField(max_length=123)),
                ('top', models.CharField(max_length=123)),
                ('topicType', models.CharField(max_length=123)),
                ('isGreat', models.CharField(max_length=123)),
                ('isAnnouncement', models.CharField(max_length=123)),
                ('phId', models.CharField(max_length=123)),
                ('subType', models.CharField(max_length=123)),
                ('vote_setting', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=123)),
                ('username', models.CharField(max_length=123)),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mock.user'),
        ),
        migrations.AddField(
            model_name='feedhottopicresponse',
            name='summery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mock.FeedTopicSummary'),
        ),
        migrations.AddField(
            model_name='favorite_programs',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mock.topic'),
        ),
    ]
