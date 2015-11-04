# -*- coding: utf-8 -*-

from django.http.response import HttpResponse

from lib.views import TemplateView


class ForumHomeView(TemplateView):
    template_name = 'forum/home.html'

    def get(self, request, *args, **kwargs):
        template = self.get_template_instance()
        return HttpResponse(template.render(**self.get_context_data()))
