# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import TextResponse
from scrapy.http.request import Request
import pathlib

class MdiDeedSpider(scrapy.Spider):
    name = 'mdideedspider'
    allowed_domains = ['vfthomas.com']

    def start_requests(self):
        start_urls = ['http://www.vfthomas.com/MDI%20Cultural%20History%20Project/MDIdeedshome.htm']
        pathlib.Path('deeds').mkdir(parents=True, exist_ok=True)
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.xpath("//body//a/@href").extract()
        for link in links[1:]:
            url = 'http://www.vfthomas.com/MDI%20Cultural%20History%20Project/' + link
            yield Request(url=url, callback = self.parse_item)

    def parse_item(self, response):   
        print('Response:' + response.url)     
        filename = 'deeds/' + response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
          