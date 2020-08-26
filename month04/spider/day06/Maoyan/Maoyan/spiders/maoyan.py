# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']

    def parse(self, response):
        dd_list = response.xpath('//dl/dd')
        for dd in dd_list:
            item = MaoyanItem()
            item['name']=dd.xpath('').get()
            item['star']=dd.xpath('').get()
            item['time']=dd.xpath('').get()

            yield item
