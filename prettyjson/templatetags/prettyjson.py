# -*- coding: utf-8 -*-

import json

from django.conf import settings
from django.template import Library
from django.forms.widgets import Media
from django.utils.safestring import mark_safe

import six

from ..widgets import PrettyJSONWidget
from ..encoders import JSONEncoder

register = Library()


@register.simple_tag
def prettyjson_setup():
    widget = PrettyJSONWidget()
    extra = '' if settings.DEBUG else '.min'
    media = Media(js=('admin/js/vendor/jquery/jquery%s.js' % extra,
                      'admin/js/jquery.init.js',)) + widget.media
    return mark_safe(str(media))


@register.simple_tag
def prettyjson(object):
    if isinstance(object, six.string_types):
        data = json.loads(object)
    else:
        data = JSONEncoder(object)
    widget = PrettyJSONWidget()
    return mark_safe(widget.render(name=None,
                     value=(json.dumps(data, ensure_ascii=False))))
