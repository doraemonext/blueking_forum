# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u4e3a\u8d85\u7ea7\u7ba1\u7406\u5458'),
        ),
    ]
