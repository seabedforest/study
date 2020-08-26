"""
建立私密代理的代理ip
思路:
    1:提取私密代理
    2：依次测试，把能用的代理ip保存
"""





import requests
class ProxyPool:
    def __init__(self):


        self.api_url='http://dps.kdlapi.com/api/getdps/?orderid=999'