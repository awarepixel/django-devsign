# -*- coding: utf-8 -*-
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
from devsign import VERSION

try:
    README = open('README.rst').read()
except:
    README = None

try:
    REQUIREMENTS = open('requirements.txt').read()
except:
    REQUIREMENTS = None

setup(name = 'django-devsign',
    version = VERSION,
    description = 'Development HTML Sign',
    long_description = README,
    install_requires = REQUIREMENTS,
    author = 'Carlos Palol',
    author_email = 'carlos.palol@awarepixel.com',
    url = 'http://www.awarepixel.com',
    packages = find_packages(),
    include_package_data = True,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    )