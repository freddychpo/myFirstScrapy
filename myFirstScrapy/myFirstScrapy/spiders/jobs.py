# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

#class JobsSpider(scrapy.Spider):
class JobsSpider(CrawlSpider):
    name = 'jobs'
    allowed_domains = ['www.python.org']
    start_urls = ['http://www.python.org/',
                'https://www.python.org/jobs/']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.list-recent-jobs',)),
             callback="parse_item",
             follow=True),)

    def parse(self, response):
        pass

    def parse_item(self, response):
        print('Extracting…' + response.url)
