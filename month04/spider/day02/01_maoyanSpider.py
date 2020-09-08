"""
猫眼电影top100数据抓取
"""
import requests, re, time, random, csv


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'Cooker': '__mta=150769929.1596618943304.1598873751664.1598873758900.27; uuid_n_v=v1; uuid=3BE0EAC0D6FC11EA915A0DDBDFA8C0BCCE9D6AE6F58C475AAFBEF814614D5749; _lxsdk_cuid=173bde7aaa2c8-08bd79edad3da-317f0a5e-1b2142-173bde7aaa4c8; _lxsdk=3BE0EAC0D6FC11EA915A0DDBDFA8C0BCCE9D6AE6F58C475AAFBEF814614D5749; mojo-uuid=08d1d1af724c18086b6e13973a6db21c; _csrf=16d21ae537d1b52fc7ec0041250814ed362e68bd80d1a0e4c89fafbcdc0334f1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1596764070,1597127976,1597221694,1598873576; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mojo-session-id={"id":"3f16cd5383e4bae902d82367e36e04ec","time":1598873576556}; __mta=150769929.1596618943304.1597127976091.1598873587061.22; mojo-trace-id=15; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598873759; _lxsdk_s=174444aa452-123-5d6-6e3%7C%7C19',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
        }


    def get_html(self, url):
        """請求"""
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """正則提取数据"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        # 直接调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        """数据处理函数"""
        for rt in r_list:
            item = {}
            item['name'] = rt[0].strip()
            item['star'] = rt[1].strip()
            item['time'] = rt[2].strip()
            print(item)


    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            self.get_html(page_url)
            # 控制频率
            time.sleep(random.uniform(1, 2))

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
