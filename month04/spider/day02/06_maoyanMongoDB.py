"""
抓取猫眼top100数据抓取-mongodb

"""
import requests
import re
import time
import random
import pymongo


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
        #创建mongo三个对象
        self.conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db = self.conn['maoyandb']
        self.myset = self.db['maoyanset']

    def get_html(self, url):
        """请求"""
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """正则提取数据"""
        regex = '<div class="board-item-content">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        pattern = re.compile(regex, re.S)
        result = pattern.findall(html)
        # 直接调用数据处理函数
        self.save_html(result)

    def save_html(self, result):
        """数据处理函数"""
        ins = 'insert into maoyantab values(%s,%s,%s)'
        for rt in result:
            item = {}
            item['name'] = rt[0].strip()
            item['str'] = rt[1].strip()
            item['time'] = rt[1].strip()
            self.myset.insert_one(item)
            print(item)

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            self.get_html(page_url)
            # 控制频率
            time.sleep(random.randint(1, 2))

        # 所有页的数据抓取完成后，断开数据库连接
        self.conn.close()


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
