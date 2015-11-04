# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('displayorder', models.IntegerField(default=0, verbose_name='\u663e\u793a\u987a\u5e8f')),
                ('threads', models.BigIntegerField(default=0, verbose_name='\u4e3b\u9898\u6570\u91cf')),
                ('posts', models.BigIntegerField(default=0, verbose_name='\u5e16\u5b50\u6570\u91cf')),
                ('today_posts', models.BigIntegerField(default=0, verbose_name='\u4eca\u65e5\u53d1\u5e16\u6570\u91cf')),
                ('yesterday_posts', models.BigIntegerField(default=0, verbose_name='\u6628\u65e5\u53d1\u5e16\u6570\u91cf')),
                ('parent', models.ForeignKey(default=0, verbose_name='\u4e0a\u7ea7\u8bba\u575b', to='forum.Forum')),
            ],
            options={
                'db_table': 'forum',
                'verbose_name': '\u677f\u5757',
                'verbose_name_plural': '\u677f\u5757',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.BooleanField(default=False, verbose_name='\u662f\u5426\u662f\u9996\u8d34')),
                ('dateline', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('message', models.TextField(verbose_name='\u6d88\u606f\u5185\u5bb9')),
                ('anonymous', models.BooleanField(default=False, verbose_name='\u662f\u5426\u533f\u540d')),
                ('author', models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(verbose_name='\u6240\u5c5e\u677f\u5757', to='forum.Forum')),
            ],
            options={
                'db_table': 'post',
                'verbose_name': '\u5e16\u5b50',
                'verbose_name_plural': '\u5e16\u5b50',
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255, verbose_name='\u6807\u9898')),
                ('read_perm', models.SmallIntegerField(default=0, verbose_name='\u9605\u8bfb\u6743\u9650')),
                ('dateline', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65e5\u671f')),
                ('last_post', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u53d1\u8868\u65e5\u671f')),
                ('views', models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u6b21\u6570')),
                ('replies', models.IntegerField(default=0, verbose_name='\u56de\u590d\u6b21\u6570')),
                ('stick', models.BooleanField(default=False, verbose_name='\u662f\u5426\u7f6e\u9876')),
                ('highlight', models.BooleanField(default=False, verbose_name='\u662f\u5426\u9ad8\u4eae')),
                ('digest', models.BooleanField(default=False, verbose_name='\u662f\u5426\u7cbe\u534e')),
                ('recommend_add', models.IntegerField(default=0, verbose_name='\u652f\u6301\u4eba\u6570')),
                ('recommend_sub', models.IntegerField(default=0, verbose_name='\u53cd\u5bf9\u4eba\u6570')),
                ('favtimes', models.IntegerField(default=0, verbose_name='\u4e3b\u9898\u6536\u85cf\u6b21\u6570')),
                ('author', models.ForeignKey(related_name='author', verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(verbose_name='\u6240\u5c5e\u677f\u5757', to='forum.Forum')),
                ('last_poster', models.ForeignKey(related_name='last_poster', verbose_name='\u6700\u540e\u53d1\u8868\u4eba', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'thread',
                'verbose_name': '\u4e3b\u9898',
                'verbose_name_plural': '\u4e3b\u9898',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u4e3b\u9898', to='forum.Thread'),
        ),
    ]
