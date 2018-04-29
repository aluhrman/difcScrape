# -*- coding: utf-8 -*-

import scrapy

class DifcItem(scrapy.Item):

    sourceId = scrapy.Field()
    crawlerId = scrapy.Field()
    recordId = scrapy.Field()
    url = scrapy.Field()
    headers = scrapy.Field()
    statusCode = scrapy.Field()
    content = scrapy.Field()

    pass
