# -*- coding: utf-8 -*-
from django.conf import settings

# Automated settings override
# This should be set to the common prefix for this application settings
# Only settings with this prefix will be overriden by main settings.py
_APPCONF_PREFIX = 'DEVSIGN'

DEVSIGN_BASE_HTML = '<div id="devsign-message" style="%(style)s">%(message)s</div>'

# The example messages dictionary defines a custom message and style
# for site with ID 2
DEVSIGN_SITE_MESSAGES = {
    2: {
        'message': 'You are using the DEVELOPMENT site.',
        'style': 'background-color: purple; color: white; font-size: 16px; padding: 12px;'
    }
}


# Automated settings override
# Expects an attribute _APPCONF_PREFIX to be available
(_k,_v) = (None,None)
for _k,_v in globals().items():
    if _k.startswith(_APPCONF_PREFIX):
        globals()[_k] = getattr(settings, _k, _v)