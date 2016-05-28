# django-prettyjson

[![PyPi Version](https://badge.fury.io/py/django-prettyjson.png)](https://badge.fury.io/py/django-prettyjson) [![Build Status](https://travis-ci.org/kevinmickey/django-prettyjson.svg?branch=master)](https://travis-ci.org/kevinmickey/django-prettyjson)

Enables pretty JSON viewer in Django forms, admin, or templates

## Demo

See http://kevinmickey.github.io/django-prettyjson

## Installation

At the command line:

```sh
pip install django-prettyjson
```

## Configuration

Add `prettyjson` to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = (
  ...,
  'prettyjson',
)
```

## Usage

In a form or admin of a model, enable a pretty JSON viewer for a particular field:

```python
import prettyjson

class JsonForm(forms.ModelForm):
  class Meta:
    model = Test
    fields = '__all__'
    widgets = {
      'myjsonfield': PrettyJSONWidget(),
    }

class JsonAdmin(admin.ModelAdmin):
  form = JsonAdminForm
```

Enable pretty JSON viewer for every JSONField of a model:

```python
class JsonAdmin(admin.ModelAdmin):
  formfield_overrides = {
    jsonfield.JSONField: {'widget': PrettyJSONWidget }
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
* [django-jsonfield](https://github.com/bradjasper/django-jsonfield/)


Tools used in developing, testing, and/or rendering this package:

* [Cookiecutter](https://github.com/audreyr/cookiecutter)
* [cookiecutter-djangopackage] (https://github.com/pydanny/cookiecutter-djangopackage)
