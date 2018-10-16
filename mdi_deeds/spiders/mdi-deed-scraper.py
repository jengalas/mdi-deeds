# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import TextResponse
from scrapy.http.request import Request
import pathlib

class MdiDeedSpider(scrapy.Spider):
    name = 'mdideedspider'
    allowed_domains = ['mdihistory.org']
    start_urls = ['http://mdihistory.org/Cultural_History_Project/htdocs/MDIdeeds']
    pathlib.Path('deeds').mkdir(parents=True, exist_ok=True)

    def parse(self, response):
        links = response.xpath("//body//a/@href").extract()
        for link in links[1:]:
            url = 'http://mdihistory.org/Cultural_History_Project/htdocs/MDIdeeds/' + link
            yield Request(url=url, callback = self.parse_item)

    def parse_item(self, response):   
        print('Response:' + response.url)     
        filename = 'deeds/' + response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
          