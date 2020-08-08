"""
输入搜索关键字，保存页面到本地文件
"""
import requests
from urllib import parse

# 1.拼接url地址
keyword = input("请输入搜索关键字:")
params = parse.quote( keyword)
url = 'https://www.baidu.com/s?wd=%s' % params
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
# 2.发送请求获取响应内容
html = requests.get(url=url, headers=headers).text
# 3.保存数据
filename = '{}.html'.format(keyword)
with open(filename, 'w') as f:
    f.write(html)
