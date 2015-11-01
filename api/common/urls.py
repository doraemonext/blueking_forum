# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from api.common.views import LoginAPI, RegisterAPI, LogoutAPI

urlpatterns = [
    url(r'^login/$', LoginAPI.as_view(), name='login'),
    url(r'^register/$', RegisterAPI.as_view(), name='register'),
    url(r'^logout/$', LogoutAPI.as_view(), name='logout'),
]
