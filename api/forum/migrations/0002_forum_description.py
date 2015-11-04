# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='description',
            field=models.TextField(default='', verbose_name='\u63cf\u8ff0'),
            preserve_default=False,
        ),
    ]
