# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from apps.common.views import RegisterView

urlpatterns = [
    url('^register/$', RegisterView.as_view(), name='register'),
]
