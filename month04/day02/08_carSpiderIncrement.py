"""
汽车之家二级页面数据抓取 用redis实现增量抓取
"""
import requests
import re, time, random
import pymysql, redis
from hashlib import md5
import sys


class CarSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1lto1csp{}exx0/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        self.db = pymysql.connect('localhost', 'root', '123456', 'cardb', charset='utf8')
        self.cur = self.db.cursor()
        # 连接redis
        self.r = redis.Redis(host='127.0.0.1', port=6379, password='123456', db=0)

    def get_html(self, url):
        """功能函:1:发请求获取到html"""
        html = requests.get(url=url, headers=self.headers).content.decode('gb2312', 'ignore')
        return html

    def re_func(self, regex, html):
        """功能函数2：正则解析"""
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        return r_list

    def md5_url(self, url):
        """功能函数3:md5加密的函数"""
        s = md5()
        s.update(url.encode())
        return s.hexdigest()

    def parse_html(self, one_url):
        """爬虫逻辑函数"""
        one_html = self.get_html(url=one_url)
        one_regex = '<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>'
        href_list = self.re_func(one_regex, one_html)
        for href in href_list:
            two_url = 'https://www.che168.com' + href
            finger = self.md5_url(two_url)
            # 返回值为1，说明之前没有抓取过
            if self.r.sadd('car:spiders', finger) == 1:
                self.get_one_car_info(two_url)
                # 控制抓取频率 uniform(0,1)生成0到1之间的浮点数
                time.sleep(random.uniform(0, 2))
            else:
                sys.exit('更新完成')

    def get_one_car_info(self, two_url):
        """获取一辆汽车的具体数据"""
        two_html = self.get_html(url=two_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<ul class="brand-unit-item fn-clear">.*?<li>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">￥(.*?)<b>'
        car_info_list = self.re_func(two_regex, two_html)
        item = {}
        # 名字+行驶里程+上牌时间
        item['name'] = car_info_list[0][0].strip()
        item['km'] = car_info_list[0][1].strip()
        item['year'] = car_info_list[0][2].strip()
        # 类别+排量
        item['type'] = car_info_list[0][3].split('/')[0].strip()
        item['displace'] = car_info_list[0][3].split('/')[1].strip()
        # 地址+价格
        item['city'] = car_info_list[0][4].strip()
        item['price'] = car_info_list[0][5].strip()
        print(item)
        one_car_list = [
            item['name'],
            item['km'],
            item['year'],
            item['type'],
            item['displace'],
            item['city'],
            item['price']
        ]

        # 存入mysqls数据库
        ins = 'insert into cartab values(%s,%s,%s,%s,%s,%s,%s)'
        self.cur.execute(ins, one_car_list)
        self.db.commit()

    def run(self):
        for page in range(1, 6):
            page_url = self.url.format(page)
            self.parse_html(page_url)

        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    spider = CarSpider()
    spider.run()
