# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig
from django.db.models.signals import post_migrate

from system.setting.models import Setting


def init_setting_table(sender, **kwargs):
    Setting.objects.create('title', 'BlueKing 交流论坛')


class SettingAppConfig(AppConfig):
    name = 'system.setting'

    def ready(self):
        post_migrate.connect(init_setting_table, sender=self)
