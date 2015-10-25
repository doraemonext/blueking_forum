# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.http.response import HttpResponse
from django.template import RequestContext

from lib.utils.templates import template_instance


class RegisterView(TemplateView):
    template_name = 'common/register.html'

    def get(self, request, *args, **kwargs):
        template = template_instance(self.template_name)
        return HttpResponse(template.render())
