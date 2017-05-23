# django-prettyjson

[![PyPi Version](https://badge.fury.io/py/django-prettyjson.png)](https://badge.fury.io/py/django-prettyjson) [![Build Status](https://travis-ci.org/kevinmickey/django-prettyjson.svg?branch=master)](https://travis-ci.org/kevinmickey/django-prettyjson)

Enables pretty JSON viewer in Django forms, admin, or templates.  The viewer is adapted from [jQuery JSONView](https://github.com/yesmeck/jquery-jsonview).  It is compatible with almost anything: JSON stored in a string, a jsonfield (using django.contrib.postgres or [django-jsonfield](https://github.com/bradjasper/django-jsonfield/)), or any python object that can be serialized to JSON (using [standardjson](https://github.com/audreyr/standardjson)).

## Demo

See http://kevinmickey.github.io/django-prettyjson

## Installation

At the command line:

```sh
pip install django-prettyjson
```

## Configuration

Add `'prettyjson'` to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = (
  ...,
  'prettyjson',
)
```

## Usage

In a form or admin of a model, enable a pretty JSON viewer for a particular field:

```python
from prettyjson import PrettyJSONWidget

class JsonForm(forms.ModelForm):
  class Meta:
    model = Test
    fields = '__all__'
    widgets = {
      'myjsonfield': PrettyJSONWidget(),
    }

class JsonAdmin(admin.ModelAdmin):
  form = JsonForm
```

Enable pretty JSON viewer for every JSONField of a model:

```python
from django.contrib.postgres.fields import JSONField

class JsonAdmin(admin.ModelAdmin):
  formfield_overrides = {
    JSONField: {'widget': PrettyJSONWidget }
  }
```

In templates, you can also enable a pretty JSON viewer.  Use the `prettyjson` template tag with a string JSON or with objects (dicts, QuerySets, etc.) that can be serialized to a JSON.  Note that the template tag must be loaded using `{% load prettyjson %}`.  It also has CSS and JS that must be included using `{% prettyjson_setup %}`.

```htmldjango
{% extends "base.html" %}

{% load prettyjson %}

{% block header %}
  {{ block.super }}
  {% prettyjson_setup %}
{% endblock %}

{% block content %}
  {% prettyjson myqueryset %}
  {% prettyjson mydict %}
  {% prettyjson '{"hey": "guy","anumber": 243,"anobject": {"whoa": "nuts","anarray": [1,2,"thr<h1>ee"], "more":"stuff"},"awesome": true,"bogus": false,"meaning": null, "japanese":"明日がある。", "link": "http://jsonview.com", "notLink": "http://jsonview.com is great"}' %}
  {% prettyjson '{}' %}
{% endblock %}
```

The setup includes jQuery, loaded as django.jQuery to avoid namespace conflict.  If your page already includes jQuery, use `{% prettyjson_setup jquery=False %}` to avoid loading jQuery a second time.

### Configure Rendering

By default the jsonwidget will render as a raw string with a button to click to change it to parsed json. For it to render as parsed json initially, you can pass an argument:

```python
class JsonAdmin(admin.ModelAdmin):
  formfield_overrides = {
    JSONField: {'widget': PrettyJSONWidget(attrs={'initial': 'parsed'})}
  }
```

## Running Tests

In development.

```sh
source <YOURVIRTUALENV>/bin/activate
(myenv) $ pip install -r requirements-test.txt
(myenv) $ python runtests.py
```

## Credits

Dependencies, parts of code, and/or sources of inspiration:

* [jQuery JSONView](https://github.com/yesmeck/jquery-jsonview)
* [standardjson](https://github.com/audreyr/standardjson)

Tools used in developing, testing, and/or rendering this package:

* [Cookiecutter](https://github.com/audreyr/cookiecutter)
* [cookiecutter-djangopackage] (https://github.com/pydanny/cookiecutter-djangopackage)
