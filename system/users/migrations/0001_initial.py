# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import system.users.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=30, verbose_name='\u7528\u6237\u540d')),
                ('email', models.EmailField(max_length=255, verbose_name='\u7535\u5b50\u90ae\u4ef6\u5730\u5740')),
                ('nickname', models.CharField(default='', max_length=30, verbose_name='\u6635\u79f0')),
                ('is_active', models.BooleanField(default=False, verbose_name='\u662f\u5426\u6fc0\u6d3b')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6ce8\u518c\u65e5\u671f')),
            ],
            options={
                'db_table': 'users',
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
            managers=[
                ('objects', system.users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u7528\u6237\u7ec4\u540d\u79f0')),
                ('stars', models.SmallIntegerField(verbose_name='\u661f\u661f\u6570')),
            ],
            options={
                'db_table': 'groups',
                'verbose_name': '\u7528\u6237\u7ec4',
                'verbose_name_plural': '\u7528\u6237\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('read_access', models.SmallIntegerField(default=0, verbose_name='\u9605\u8bfb\u6743\u9650')),
                ('allow_post', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u53d1\u5e16')),
                ('allow_reply', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u56de\u590d')),
                ('allow_get_attach', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u4e0b\u8f7d/\u67e5\u770b\u9644\u4ef6')),
                ('allow_post_attach', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u53d1\u5e03\u9644\u4ef6')),
                ('allow_post_image', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u53d1\u5e03\u56fe\u7247')),
                ('allow_search', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u641c\u7d22')),
                ('allow_anonymous', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u533f\u540d\u53d1\u5e16')),
                ('max_signature_size', models.IntegerField(default=0, verbose_name='\u7528\u6237\u7b7e\u540d\u6700\u5927\u5b57\u8282\u6570')),
                ('max_attach_size', models.BigIntegerField(default=0, verbose_name='\u6700\u5927\u9644\u4ef6\u5c3a\u5bf8')),
                ('attach_extensions', models.CharField(default='', max_length=255, verbose_name='\u5141\u8bb8\u4e0a\u4f20\u7684\u9644\u4ef6\u6269\u5c55\u540d')),
                ('group', models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237\u7ec4', to='users.Group')),
            ],
            options={
                'db_table': 'permissions',
                'verbose_name': '\u6743\u9650',
                'verbose_name_plural': '\u6743\u9650',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237\u7ec4', to='users.Group'),
        ),
    ]
