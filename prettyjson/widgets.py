from django.forms import widgets


class PrettyJSONWidget(widgets.Textarea):
    def render(self, name, value, attrs=None):
        html = super(PrettyJSONWidget, self).render(name, value, attrs)
        return ('<div class="jsonwidget"><p><button class="parseraw" '
                'type="button">Show parsed</button> <button class="parsed" '
                'type="button">Collapse all</button> <button class="parsed" '
                'type="button">Expand all</button></p>'+html+'<div '
                'class="parsed"></div></div>')

    class Media:
        # http://stackoverflow.com/questions/7188563/django-admin-jquery-namespace
        js = ('prettyjson/js/dj.jquery.jsonview.min.js', 'prettyjson/js/prettyjson.js', )
        # https://docs.djangoproject.com/en/1.9/topics/forms/media/#css
        css = {
            'all': ('prettyjson/css/jquery.jsonview.min.css', 'prettyjson/css/prettyjson.css', )
        }
