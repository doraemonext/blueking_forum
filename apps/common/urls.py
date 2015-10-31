# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from apps.common.views import RegisterView, LoginView, ForgotPasswordView

urlpatterns = [
    url('^register/$', RegisterView.as_view(), name='register'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^forgot_password/$', ForgotPasswordView.as_view(), name='forgot_password'),
]
