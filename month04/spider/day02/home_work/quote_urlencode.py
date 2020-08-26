"""
quote、urlencode处理url地址
"""
from urllib import parse

# quote方法处理
url = 'http://tencent.com/q?city={}&keyword={}&index=1'
city = parse.quote('北京')
keyword = parse.quote('爬虫')
url = url.format(city, keyword)
print(url)

# urlencode方法处理
url = 'http://tencent.com/q?{}'
params = {
    'city': '北京',
    'keyword': '爬虫',
    'index': 1
}
params = parse.urlencode(params)
url = url.format(params)
print(url)
