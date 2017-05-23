#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

version = get_version('prettyjson', '__init__.py')

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

# bumpversion does this
# if sys.argv[-1] == 'tag':
#     print("Tagging the version on github:")
#     os.system("git tag -a %s -m 'version %s'" % (version, version))
#     os.system("git push --tags")
#     sys.exit()

readme = open('README.md').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-prettyjson',
    version=version,
    description="""Enables pretty JSON viewer in Django forms, admin, or templates""",
    long_description=readme + '\n\n' + history,
    author='Kevin Mickey',
    author_email='kwmickey@gmail.com',
    url='https://github.com/kevinmickey/django-prettyjson',
    packages=[
        'prettyjson',
    ],
    include_package_data=True,
    install_requires=[
        'django>=1.8',
        'standardjson>=0.3.1',
        'six>=1.10.0'
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-prettyjson',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
