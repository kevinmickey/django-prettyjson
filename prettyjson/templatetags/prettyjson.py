# -*- coding: utf-8 -*-

import json

from django.template import Library
from django.utils.safestring import mark_safe

import six

from ..widgets import PrettyJSONWidget
from standardjson import StandardJSONEncoder

register = Library()


@register.simple_tag
def prettyjson_setup(jquery=True):
    widget = PrettyJSONWidget()
    media = widget.media
    if not jquery:
        media._js = media._js[2:]
    return mark_safe(str(media))


@register.simple_tag
def prettyjson(obj, name="", **kwargs):
    data = obj
    if isinstance(obj, six.string_types):
        data = json.loads(obj)
    widget = PrettyJSONWidget(attrs=kwargs)
    return mark_safe(widget.render(name=name,
                     value=(json.dumps(data, ensure_ascii=False, cls=StandardJSONEncoder)),
                     attrs=widget.attrs))
