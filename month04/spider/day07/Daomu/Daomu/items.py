# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 存储目录  小标题  小说内容
    directory = scrapy.Field()
    son_title = scrapy.Field()
    content = scrapy.Field()
