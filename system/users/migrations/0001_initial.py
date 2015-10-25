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
                ('nickname', models.CharField(default=b'', max_length=30, verbose_name='\u6635\u79f0')),
                ('is_active', models.BooleanField(default=False, verbose_name='\u662f\u5426\u6fc0\u6d3b')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6ce8\u518c\u65e5\u671f')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'db_table': 'user',
            },
            managers=[
                ('objects', system.users.models.UserManager()),
            ],
        ),
    ]
