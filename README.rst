=============================
django-prettyjson
=============================

.. image:: https://badge.fury.io/py/django-prettyjson.png
    :target: https://badge.fury.io/py/django-prettyjson

.. image:: https://travis-ci.org/kevinmickey/django-prettyjson.png?branch=master
    :target: https://travis-ci.org/kevinmickey/django-prettyjson

Prettify JSON in Django

Installation
------------

At the command line::

    pip install django-prettyjson

Usage
-----

Then use it in a project::

    import prettyjson

    class JsonForm(forms.ModelForm):
      class Meta:
        model = Test
        fields = '__all__'
        widgets = {
          'json': PrettyJSONWidget(),
        }

    class JsonAdmin(admin.ModelAdmin):
      form = JsonAdminForm

    class JsonAdmin(admin.ModelAdmin):
      formfield_overrides = {
        jsonfield.JSONField: {'widget': PrettyJSONWidget }
      }

    {% extends "base.html" %}

    {% load prettyjson %}

    {% block css %}
    {{ block.super }}
    {% prettyjson_setup %}
    {% endblock %}

    {% block content %}
    {% prettyjson '{"hey": "guy","anumber": 243,"anobject": {"whoa": "nuts","anarray": [1,2,"thr<h1>ee"], "more":"stuff"},"awesome": true,"bogus": false,"meaning": null, "japanese":"明日がある。", "link": "http://jsonview.com", "notLink": "http://jsonview.com is great"}' %}
    {% prettyjson '{}' %}
    {% endblock %}

Features
--------

* TODO

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
