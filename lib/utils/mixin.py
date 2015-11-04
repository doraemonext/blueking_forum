# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin as OriginLoginRequiredMixin
from braces.views import AnonymousRequiredMixin as OriginAnonymousRequiredMixin


class LoginRequiredMixin(OriginLoginRequiredMixin):
    def get_login_url(self):
        return reverse('common:login')


class AnonymousRequiredMixin(OriginAnonymousRequiredMixin):
    def get_authenticated_redirect_url(self):
        return reverse('ucenter:home')
