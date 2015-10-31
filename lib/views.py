# -*- coding: utf-8 -*-

from django.views.generic import TemplateView as DjangoTemplateView
from django.conf import settings
from django.template import Context
from mako.lookup import TemplateLookup


class TemplateView(DjangoTemplateView):
    def get_context_data(self, **kwargs):
        return settings.CONSTANT

    def get_template_instance(self):
        lookup = TemplateLookup(
            directories=settings.TEMPLATES[0]['DIRS'],
            input_encoding='utf-8',
            output_encoding='utf-8',
        )
        return lookup.get_template(self.template_name)
