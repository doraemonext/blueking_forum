# -*- coding: utf-8 -*-

from system.setting.models import Setting


def setting(request):
    return {'setting': Setting.objects.get_all()}
