"""
中国电影库-票房排行榜
"""
import requests
import re
import time
import random
from lxml import etree
from fake_useragent import UserAgent


class MoviesSpider:
    def __init__(self):
        self.url = 'http://58921.com/alltime?page={}'

    def get_html(self, url):
        """功能函数1:发送请求获取html"""
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')
        return html

    def re_func(self, regex, html):
        """功能函数2:正则解析"""
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        return r_list

    def parse_html(self, one_url):
        """爬虫逻辑函数"""
        one_html = self.get_html(url=one_url)
        one_regex_odd = '<tr class="even">.*?<a href="(.*?)".*?</a>'
        one_regex_even = '<tr class="odd">.*?<a href="(.*?)".*?</a>'
        #爬取奇数链接
        href_list = self.re_func(one_regex_odd, one_html)
        for href in href_list:
            # print(href)
            # /film/(.*?)
            two_href = 'http://58921.com' + href
            # print(href)
            number = int(re.findall(r"\d+", href)[0])
            self.get_one_movie(two_href, number)
            time.sleep(random.uniform(0, 1))
        # 爬取偶数链接
        href_list = self.re_func(one_regex_even, one_html)
        for href in href_list:
            # print(href)
            # /film/(.*?)
            two_href = 'http://58921.com' + href
            # print(href)
            number = int(re.findall(r"\d+", href)[0])
            self.get_one_movie(two_href, number)
            time.sleep(random.uniform(0, 1))

    def get_one_movie(self, two_href, number):
        """获取二级页面详细信息"""
        two_html = self.get_html(two_href)
        print(two_html)
        # Xpath提取数据
        # print(number)
        p = etree.HTML(two_html)
        # print('//*[@id="content_view_{}"]/div[2]/div/ul'.format(number))
        dd_list = p.xpath('//*[@id="content_view_{}"]/div[2]/div/ul'.format(number))
        # //*[@id="content_view_5331"]/div[2]/div/ul
        print('dd_list ******',dd_list)
        for dd in dd_list:
            item = {}
            item['票房链接'] = dd.xpath('.//li[1]/a/@href')
            item['导演'] = dd.xpath('.//li[2]/a/text()')
            item['上映时间'] = dd.xpath('.//li[4]/text()')
            item['片长'] = dd.xpath('.//li[5]/text()')
            item['类型'] = dd.xpath('.//li[7]/a/text()')
            print(item)

    def run(self):
        """入口函数"""
        for page in range(2, 4):
            page_url = self.url.format(page)
            print(page_url)
            self.parse_html(page_url)
            print('第{}页打印完毕'.format(page))
            time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    spider = MoviesSpider()
    spider.run()
