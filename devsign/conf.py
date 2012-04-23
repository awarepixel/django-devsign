# -*- coding: utf-8 -*-
from django.conf import settings

# Devsign template
DEVSIGN_BASE_HTML = '<div id="devsign-message" style="{style}">{message}</div>'

# The example messages dictionary defines a custom message and style
# for "domain development.example.org"
DEVSIGN_MESSAGES = {
    'development.example.org': {
        'message': 'You are using the DEVELOPMENT site.',
        'style': 'background-color: purple; color: white; font-size: 16px; padding: 12px;'
    }
}


PREFIX = 'DEVSIGN'
# App Settings Override 0.2
# https://gist.github.com/1925449
# * Set your app settings prefix
# * Keep this script **after** constant settings,
#   and **before** calculated settings
import sys; from django.conf import settings
for k,v in locals().items():
    if k.startswith(PREFIX):
        setattr(sys.modules[__name__], k, getattr(settings, k, v))