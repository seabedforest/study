"""
4567tv电影信息抓取
MySQL数据库建库建表: 指纹表
create database tvdb charset utf8;
use tvdb;
create table tv_finger(
finger char(32)
)charset=utf8;
"""
import requests, re, time, random, pymysql, pymongo, sys
from hashlib import md5


class TvSpider(object):
    def __init__(self):
        self.one_url = 'https://www.4567tv.tv/index.php/vod/show/id/5/page/{}.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'cookie': 'UM_distinctid=1742f97ee166eb-03657bd3c3acfb-317f0a5e-1b2142-1742f97ee172b0; CNZZDATA1272718683=549633270-1598525973-%7C1598525973; Hm_lvt_ac35181395181065b229caf707912ee5=1598526320; Hm_lvt_f90b662e460cad90d8d7bc5aea01a1a5=1598526320; Hm_lpvt_ac35181395181065b229caf707912ee5=1598527836; Hm_lpvt_f90b662e460cad90d8d7bc5aea01a1a5=1598527837'}

        # mysql
        self.db = pymysql.connect('localhost', 'root', '123456', 'tvdb', charset='utf8')
        self.cur = self.db.cursor()
        # MongoDB
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.mongo_db = self.conn['tvdb']
        self.myset = self.mongo_db['tvset']

    def get_html(self, url):
        """获取响应内容功能函数"""
        html = requests.get(url=url, headers=self.headers).content.decode('utf-8')
        return html

    def regex_func(self, regex, html):
        """正则解析功能函数"""
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        return r_list

    def md5_url(self, url):
        """生成指纹功能函数"""
        s = md5()
        s.update(url.encode())
        return s.hexdigest()

    def parse_html(self, one_url):
        """开始进行数据抓取"""
        one_html = self.get_html(one_url)
        one_regex = '<li class="col-md-6 col-sm-4 col-xs-3">.*?href="(.*?)".*?</li>'
        href_list = self.regex_func(one_regex, one_html)
        for href in href_list:
            two_url = 'https://www.4567tv.tv' + href
            # 开始进行指纹判断
            finger = self.md5_url(two_url)
            sel = 'select * from tv_finger where finger=%s'
            result = self.cur.execute(sel, [finger])
            if not result:
                # 指纹表中不存在，则进行数据抓取抓取完成后并将指纹存入指纹表
                self.get_data(two_url)
                ins = 'insert into tv_finger value (%s)'
                self.cur.execute(ins, [finger])
                self.db.commit()
                time.sleep(random.uniform(0, 1))
            else:
                sys.exit('数据更新完成')

    def get_data(self, two_url):
        """具体获取电影信息数据"""
        two_html = self.get_html(two_url)
        two_regex = '<div class="stui-content__detail">.*?<h1 class="title">(.*?)</h1>.*?<span class="detail-content" style="display: none;">(.*?)</span>'
        film_list = self.regex_func(two_regex, two_html)
        item = {}
        item['film_name'] = film_list[0][0]
        item['film_content'] = film_list[0][1]
        print(item)
        # 将所抓取数据存入MongoDB数据库
        self.myset.insert_one(item)

    def run(self):
        for i in range(1, 11):
            one_url = self.one_url.format(i)
            self.parse_html(one_url)


if __name__ == '__main__':
    spider = TvSpider()
    spider.run()
