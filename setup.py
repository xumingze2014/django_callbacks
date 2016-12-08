
#!/usr/bin/env python

import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'Readme.md')).read()

requires = [
    'requests>=2.7',
]

includes = (
    'django_callbacks',
)

setup(
    name="sms-provider-python",
    version='0.1.0',
    packages=find_packages(),
    install_requires=requires,
    description='django_callbacks',
    long_description=README,
    author="zhumengyuan",
    license="BSD",
    url=""
)