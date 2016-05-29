# -*- coding: utf-8 -*-

import json

from django.conf import settings
from django.template import Library
from django.forms.widgets import Media
from django.utils.safestring import mark_safe

import six

from ..widgets import PrettyJSONWidget
from standardjson import StandardJSONEncoder

register = Library()


@register.simple_tag
def prettyjson_setup(jquery=True):
    widget = PrettyJSONWidget()
    extra = '' if settings.DEBUG else '.min'
    if jquery:
        media = Media(js=('admin/js/vendor/jquery/jquery%s.js' % extra,
                          'admin/js/jquery.init.js',)) + widget.media
    else:
        media = widget.media
    return mark_safe(str(media))


@register.simple_tag
def prettyjson(obj):
    data = obj
    if isinstance(object, six.string_types):
        data = json.loads(obj)
    widget = PrettyJSONWidget()
    return mark_safe(widget.render(name=None,
                     value=(json.dumps(data, ensure_ascii=False, cls=StandardJSONEncoder))))
