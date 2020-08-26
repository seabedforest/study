import requests,re,time,random

class FilmSkySpider:
    def __init__(self):
        """定义常用变量"""
        #一级页面url地址
        self.one_url='https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'