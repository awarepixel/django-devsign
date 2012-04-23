# -*- coding: utf-8 -*-
import re
from django.utils.encoding import smart_str
from devsign import conf


_BODY_RE = re.compile(r'<body([^<]*)>', re.IGNORECASE)

class DevsignMiddleware(object):
    def process_response(self, request, response):
        host = request.get_host()
        if host in conf.DEVSIGN_MESSAGES:
            html = conf.DEVSIGN_BASE_HTML.format(**conf.DEVSIGN_MESSAGES[host])
            response.content = _BODY_RE.sub(smart_str('<body\\1>' + html), response.content)
        
        return response
