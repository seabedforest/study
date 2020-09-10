import requests
from lxml import etree
import random, time

# 帖子链接，想要提取帖子中视频的链接
url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E8%83%A1%E6%AD%8C&fr=search'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}

html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')
p = etree.HTML(html)
# 以响应内容为准来写xpath或者正则表达式
src_list = p.xpath('//div[@class="threadlist_video"]/a/@data-video')
for url in src_list:
    name = 'fugu_video/'+url[-20:]
    html = requests.get(url=url, headers=headers).content
    with open(name, 'wb') as f:
        f.write(html)
    print(name, '已经下载完毕')
    time.sleep(random.uniform(1, 2))
