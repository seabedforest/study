"""
有道翻译破解
思路:
    1、F12刷新页面抓包
    2、Network-XHR-Preview找到了具体返回数据的网络数据包
    3、分析此数据包
       3.1> Headers-General 找到了 Request URL (post的地址)
       3.2> Headers-Requests Headers(请求头)
       3.3> Form Data 找到了Form表单的数据
    4、发现Form表单数据有加密
       4.1> 页面执行行为,分析对比加密的数据
       4.2> 找到相关JS，并分析查看JS代码（可能用到断点调试）
       4.3> Python按照相同的加密方式实现一遍
"""
import requests, time, random
from hashlib import md5


class YdSpider:
    def __init__(self):
        # post_url:一定要为f12抓包抓到的地址
        self.post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            # Cookie Referer User-Agent 检查频率最高的
            "Cookie": "OUTFOX_SEARCH_USER_ID=-287639189@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=2020339196.0389502; JSESSIONID=aaaxXK_uspSjecJ8Sn7rx; ___rl__test__cookies=1599795607978",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
        }

    def get_ts_salt_sign(self, word):
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        # sign:
        string = "fanyideskweb" + word + salt + "]BjuETDhU)zqSxf-=B#7m"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()
        return ts, salt, sign

    def attack_yd(self, word):
        ts, salt, sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": ts,
            "bv": "80c36af3353d0267ec8eb62c23ad618c",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }

        html = requests.post(url=self.post_url, data=data, headers=self.headers).json()
        result = html['translateResult'][0][0]['tgt']

        return result

    def run(self):
        word = input('请输入要翻译的单词:')
        print(self.attack_yd(word))


if __name__ == '__main__':
    spider = YdSpider()
    spider.run()
