import django

from django.conf import settings
from django.forms import widgets

if django.VERSION >= (2, 0, 0):
    from django.utils.translation import gettext as _
else:
    from django.utils.translation import ugettext as _


class PrettyJSONWidget(widgets.Textarea):

    DEFAULT_ATTR = 'raw'

    def render(self, name, value, attrs=None, **kwargs):
        html = super(PrettyJSONWidget, self).render(name, value, attrs)

        start_as = self.attrs.get("initial", self.DEFAULT_ATTR)

        if (start_as not in self._allowed_attrs()):
            start_as = self.DEFAULT_ATTR

        return (
            '<div class="jsonwidget" data-initial="' + start_as + '"> '
            '<p> '
            '<button class="parseraw btn-parsed" type="button">' + _("Show parsed") + '</button> '
            '<button class="parsed btn-raw" type="button">' + _("Show raw") + '</button> '
            '<button class="parsed btn-collapse" type="button">' + _("Collapse") + '</button> '
            '<button class="parsed btn-expand" type="button">' + _("Expand") + '</button> '
            '</p>' + html + '<div class="parsed"></div> '
            '</div>'
        )

    @staticmethod
    def _allowed_attrs():
        return (PrettyJSONWidget.DEFAULT_ATTR, 'parsed')

    @property
    def media(self):
        extra = '' if settings.DEBUG else '.min'
        return widgets.Media(
            js=(
                'admin/js/vendor/jquery/jquery%s.js' % extra,
                'admin/js/jquery.init.js',
                'prettyjson/prettyjson.js',
            ),
            css={
                'all': ('prettyjson/prettyjson.css', )
            },
        )
