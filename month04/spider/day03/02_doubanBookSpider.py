import requests
from lxml import etree
import random, time
from fake_useragent import UserAgent


class DoubanBookSpider:
    def __init__(self):
        self.url = 'https://book.douban.com/top250?start={}'

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).content.decode('utf8', 'ignore')
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """lxml+xpath解析提取数据"""
        p = etree.HTML(html)
        table_list = p.xpath('//div[@class="indent"]/table')
        for table in table_list:
            item = {}
            # 书名
            name_list = table.xpath('.//div[@class="pl2"]/a/@title')
            item['name'] = name_list[0].strip() if name_list else None
            # 描述
            content_list = table.xpath('.//p[@class="pl"]/text()')
            item['content'] = content_list[0].strip() if content_list else None
            # 评分
            score_list = table.xpath('.//span[@class="rating_nums"]/text()')
            item['score'] = score_list[0].strip() if score_list else None
            # 评价人数
            nums_list = table.xpath('.//span[@class="pl"]/text()')
            item['nums'] = nums_list[0][1:-1].strip() if nums_list else None
            # 类别
            type_list = table.xpath('.//span[@class="inq"]/text()')
            item['type'] = type_list[0].strip() if type_list else None
            print(item)

    def run(self):
        for page in range(1, 6):
            start = (page - 1) * 25
            page_url = self.url.format(start)
            self.get_html(url=page_url)
            # 控制频率
            time.sleep(random.uniform(1, 3))


if __name__ == '__main__':
    spider = DoubanBookSpider()
    spider.run()
