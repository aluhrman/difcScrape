# -*- coding: utf-8 -*-
import hashlib
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from difc.items import DifcItem

def complete_url(string):
    return "http://www.difc.ae" + string


class DifcSpider(CrawlSpider):
    name = "difcSpider"
    allowed_domains = ["difc.ae"]
    start_urls = ["http://www.difc.ae/browse-directory?page=0"]
    rules = (
        Rule (LinkExtractor(allow='page=', restrict_xpaths='//li[@class="pager-next"]'), callback='parse_directory'),
    )

    def parse(self, response):
        sel = Selector(response)
        lastPage = sel.xpath('//li[@class="pager-last last"]/a/@href').extract()[0].split('=')[1]

        for n in range(0, int(lastPage)):
            yield scrapy.Request("http://www.difc.ae/browse-directory?page="+str(n), callback=self.parse_directory)



    def parse_directory(self, response):

        sel = Selector(response)
        sites = sel.xpath('/html/body/div/div/div[4]/div/div/div/div/div/div[2]/div/table/tbody/tr/td/a/@href')

        for site in sites:
            link = site.extract()
            yield scrapy.Request(complete_url(link), callback=self.parse_record)


    def parse_record(self, response):

        record = []
        items = DifcItem()

        sourceId = "aedifc"

        items['sourceId'] = sourceId
        items['url'] = response.url
        items['headers'] = response.headers
        items['statusCode'] = response.status
        items['content'] = response.body


        urlHash = hashlib.sha1(response.url).hexdigest()
        makeId = sourceId + urlHash
        recordId = hashlib.sha1(makeId).hexdigest()

        items['recordId'] = recordId
        record.append(items)

        return record

