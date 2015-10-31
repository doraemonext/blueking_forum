# -*- coding: utf-8 -*-

from django.http.response import HttpResponse

from lib.views import TemplateView


class UCenterHomeView(TemplateView):
    template_name = 'ucenter/home.html'

    def get(self, request, *args, **kwargs):
        template = self.get_template_instance()
        return HttpResponse(template.render(**self.get_context_data()))
