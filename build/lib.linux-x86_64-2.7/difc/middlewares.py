# -*- coding: utf-8 -*-

import os
from scrapy.conf import settings

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://aproxy:2605"

