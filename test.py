import re,os,hashlib,requests
from bs4 import BeautifulSoup
from Crypto.Cipher import AES

class Tedu:
    def __init__(self):
        self.session = requests.Session()
        self.loginName = ''
        self.password = ''
        self.down_url = 'http://c.it211.com.cn/'
        self.path = './download/'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'http://www.tmooc.cn/',
        }

    def login(self):
        self.session.get('http://uc.tmooc.cn/userValidata/getUserInfo')
        data={
            'loginName': self.loginName,
            'password': hashlib.md5(self.password.encode(encoding='UTF-8')).hexdigest(),
            'accountType': '1'
        }

        self.session.get('http://uc.tmooc.cn/login',data=data)
        requests.utils.add_dict_to_cookiejar(self.session.cookies,{'isCenterCookie':'yes'})
        a=self.session.get('http://tts.tmooc.cn/user/myTTS',
                         params={'sessionId': self.session.cookies.get_dict()['TMOOC-SESSION']})
        print('xxxqqq',a.content.decode('utf-8'))
        try:
            self.session.cookies.get_dict()['sessionid']
            print('登录成功')
            return True
        except:
            print('登录失败')
            return False


a=Tedu()
a.login()

