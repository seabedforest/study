"""
向京东官网发送请求，获取内容
"""
import requests

res = requests.get(url='https://www.jd.com')
# 属性1：text 获取响应内容-字符串
# print(res.text)
# 属性2：content 获取响应内容—字节串(bytes)，只要用于抓取图片、音频、视频、文件
# print(res.content)
# 属性3：获取http响应码
print(res.status_code)
# 属性4:返回实际数据的URL地址
print(res.url)
