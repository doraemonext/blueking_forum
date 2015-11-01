# -*- coding: utf-8 -*-

from django.conf.urls import include, url

urlpatterns = [
    url(r'^common/', include('api.common.urls', namespace='common')),
    # url(r'^ucenter/', include('api.ucenter.urls', namespace='ucenter')),
]
