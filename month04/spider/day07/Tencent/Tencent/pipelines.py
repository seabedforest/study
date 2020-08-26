# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道1 终端输出数据
class TencentPipeline(object):
    def process_item(self, item, spider):
        print(dict(item))
        return item


# 管道2 mysql数据持久化
import pymysql
from .settings import *


class TencentMysqlPipeline(object):
    def open_spider(self, spider):
        # 爬虫项目开始时，只执行一次，一般用于数据库的连接
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_DB, charset=CHARSET)
        self.cur = self.db.cursor()
        self.ins = 'insert into tencenttab values(%s,%s,%s,%s,%s,%s)'

    def process_item(self, item, spider):
        li = [
            item['job_name'],
            item['job_type'],
            item['job_duty'],
            item['job_require'],
            item['job_add'],
            item['job_time'],
        ]
        self.cur.execute(self.ins, li)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()


import pymongo


class TencentMongoPipeline:
    def open_spider(self, spider):
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        self.myset.insert_one(dict(item))
        return item
