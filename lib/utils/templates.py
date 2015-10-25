# -*- coding: utf-8 -*-

from django.conf import settings
from mako.template import Template
from mako.lookup import TemplateLookup


def template_instance(path):
    mylookup = TemplateLookup(
        directories=settings.TEMPLATES[0]['DIRS'],
        input_encoding='utf-8',
        output_encoding='utf-8',
    )
    return mylookup.get_template(path)
