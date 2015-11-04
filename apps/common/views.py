# -*- coding: utf-8 -*-

from django.http.response import HttpResponse

from lib.views import TemplateView
from lib.utils.mixin import AnonymousRequiredMixin


class RegisterView(AnonymousRequiredMixin, TemplateView):
    template_name = 'common/register.html'

    def get(self, request, *args, **kwargs):
        template = self.get_template_instance()
        return HttpResponse(template.render(**self.get_context_data()))


class LoginView(AnonymousRequiredMixin, TemplateView):
    template_name = 'common/login.html'

    def get(self, request, *args, **kwargs):
        template = self.get_template_instance()
        return HttpResponse(template.render(**self.get_context_data()))


class ForgotPasswordView(AnonymousRequiredMixin, TemplateView):
    template_name = 'common/forgot_password.html'

    def get(self, request, *args, **kwargs):
        template = self.get_template_instance()
        return HttpResponse(template.render(**self.get_context_data()))
