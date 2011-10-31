# -*- coding: utf-8 -*-
from distutils.core import setup
from APPNAME import VERSION

setup(name = 'django-devsign',
    version = VERSION,
    description = 'Development HTML Sign',
    author = 'Carlos Palol',
    author_email = 'carlos.palol@awarepixel.com',
    url = 'http://www.awarepixel.com',
    packages = [
        'devsign',
        'package.subpackage',
        ],
    )