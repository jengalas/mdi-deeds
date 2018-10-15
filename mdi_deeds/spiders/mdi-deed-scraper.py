# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.http import TextResponse
from scrapy.spiders import CrawlSpider
from scrapy.http.request import Request

class MdiDeedSpider(scrapy.Spider):
    name = 'mdideedspider'
    allowed_domains = ['mdihistory.org']
    start_urls = ['http://mdihistory.org/Cultural_History_Project/htdocs/MDIdeeds']

    def parse(self, response):
        links = response.xpath("//body//a/@href").extract()
        for link in links[1:]:
            url = 'http://mdihistory.org/Cultural_History_Project/htdocs/MDIdeeds/' + link
            yield Request(url=url, callback = self.parse_item)

    def parse_item(self, response):   
        print('Response:' + response.url)     
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
          