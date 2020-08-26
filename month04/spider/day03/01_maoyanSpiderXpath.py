"""
抓取猫眼电影信息
"""
import requests
import re
import time
import random
from lxml import etree


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}

    def get_html(self, url):
        """请求"""
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """lxml+xpath提取数据"""
        p = etree.HTML(html)
        # 1.基准xpath,匹配每个电影的dd节点对象列表
        dd_list = p.xpath('//dl/dd')
        for dd in dd_list:
            item = {}
            item['name'] = dd.xpath('.//p[@class="name"]/a/text()')[0]
            item['str'] = dd.xpath('.//p[@class="str"]/text()')[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            print(item)
            
    # def save_html(self, result):
    #     """数据处理函数"""
    #     for rt in result:
    #         item = {}
    #         item['name'] = rt[0].strip()
    #         item['str'] = rt[1].strip()
    #         item['time'] = rt[2].strip()
    #         print(item)

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            self.get_html(page_url)
            # 控制频率
            time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
