"""
思路:
    1:打开网站:
    2.找到最新月份节点点击
    3.切换句柄
    4.使用selenium提取 名称+行政代码
"""
import sys

from selenium import webdriver
import time
import redis
from hashlib import md5


class MzbSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.url)
        self.r = redis.Redis(host='localhost', port=6379, db=0, password='123456')

    def md5_url(self, url):
        """功能函数"""
        s = md5()
        s.update(url.encode())
        return s.hexdigest()

    def parse_html(self):
        """解析提取数据"""
        a_node = self.driver.find_element_by_partial_link_text('县以上行政区划代码')
        href = a_node.get_attribute('href')
        finger = self.md5_url(url=href)
        if self.r.sadd('mzb:spider', finger) == 1:
            a_node.click()
            # 给页面元素加载预留时间
            time.sleep(1)
            # 切换句柄
            all_handles_li = self.driver.window_handles
            self.driver.switch_to_window(all_handles_li[1])
            # 切换句柄之后，开始提取数据
            tr_list = self.driver.find_elements_by_xpath('//tr[@height="19"]')
            for tr in tr_list:
                item = {}
                item['code'] = tr.text.split()[0].strip()
                item['name'] = tr.text.split()[1].strip()
                print(item)
        else:
            sys.exit('更新完成')

    def run(self):
        self.parse_html()


if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()
