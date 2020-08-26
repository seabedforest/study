# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # result = response.xpath('/html/head/title/text()')
        # result = response.xpath('/html/head/title/text()').extract()
        result = response.xpath('/html/head/title/text()').extract_first()
        print(result)
        print('*' * 50)
        # xpath()结果 [<Selector xpath='/html/head/title/text()' data='百度一下，你就知道'>]
        # extract()结果：['百度一下，你就知道']
        # extract_first()结果：'百度一下，你就知道'
        # get()结果 '百度一下，你就知道' 等同于 extract_first()
