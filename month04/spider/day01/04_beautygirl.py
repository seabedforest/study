"抓取图片"
import requests

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596617847997&di=b156eea2e905a9ba0eea8d639c9ebf65&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F2018-05-30%2F5b0e3930175f7.jpg%3Fdown'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
html = requests.get(url=url, headers=headers).content

with open('gril.jpg', 'wb') as f:
    f.write(html)
