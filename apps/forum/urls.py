# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from apps.forum.views import ForumHomeView

urlpatterns = [
    url('^home/$', ForumHomeView.as_view(), name='home'),
]
