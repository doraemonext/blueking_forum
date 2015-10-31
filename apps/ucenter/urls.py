# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from apps.ucenter.views import UCenterHomeView

urlpatterns = [
    url('^home/$', UCenterHomeView.as_view(), name='home'),
]
