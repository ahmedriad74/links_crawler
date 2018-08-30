# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class LinksSpider(CrawlSpider):
	name = 'links'
	allowed_domains = ['banffcyber.com']
	start_urls = ['https://www.banffcyber.com/']
	rules = (Rule(LinkExtractor(), callback='parse_page', follow=True),)
	
	def parse_page(self, response):
		yield{'URL':response.url}


