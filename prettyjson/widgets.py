from django.conf import settings
from django.forms import widgets


class PrettyJSONWidget(widgets.Textarea):

    DEFAULT_ATTR = 'raw'

    def render(self, name, value, attrs=None, **kwargs):
        html = super(PrettyJSONWidget, self).render(name, value, attrs)

        start_as = self.attrs.get("initial", self.DEFAULT_ATTR)

        if (start_as not in self._allowed_attrs()):
            start_as = self.DEFAULT_ATTR

        return ('<div class="jsonwidget" data-initial="' + start_as + '"><p><button class="parseraw" '
                'type="button">Show parsed</button> <button class="parsed" '
                'type="button">Collapse all</button> <button class="parsed" '
                'type="button">Expand all</button></p>' + html + '<div '
                'class="parsed"></div></div>')

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
