
#!/usr/bin/env python

import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'Readme.md')).read()

requires = [
    'requests>=2.7',
]

includes = (
    'django_callback',
)

setup(
    name="django_callbacks",
    version='0.1.0',
    packages=find_packages(),
    install_requires=requires,
    description='django_callbacks',
    long_description=README,
    author="xumingze",
    license="BSD",
    url=""
)