# -*- coding: utf-8 -*-
import re
from django.utils.encoding import smart_str
from django.contrib.sites.models import Site
from devsign import conf

_END_BODY_RE = re.compile(r'<body([^<]*)>', re.IGNORECASE)

class DevsignMiddleware(object):
    
    def __init__(self):
        current_site = Site.objects.get_current()
        self.html = False
        
        if conf.DEVSIGN_SITE_MESSAGES.has_key(current_site.id):
            message_dict = conf.DEVSIGN_SITE_MESSAGES[current_site.id]
            message_dict = {
                'message': message_dict['message'] if message_dict.has_key('message') else '',
                'style': message_dict['style'] if message_dict.has_key('style') else ''
            }
            self.html = conf.DEVSIGN_BASE_HTML % message_dict
    
    def process_response(self, request, response):
        if self.html:
            response.content = _END_BODY_RE.sub(smart_str('<body\\1>' + self.html), response.content)
        
        return response