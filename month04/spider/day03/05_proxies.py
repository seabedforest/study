"""免费代理"""
import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent': 'Mozilla/5.0'}
proxies = {
    'http': 'http://49.89.143.154:9999',
    'https': 'https://171.13.4.154:9999',
}
html = requests.get(url=url, proxies=proxies, headers=headers).text
print(html)
