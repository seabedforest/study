import re, os, hashlib, requests
# from lxml import etree
from bs4 import BeautifulSoup
from Crypto.Cipher import AES


class Tedu:
    def __init__(self):
        self.session = requests.Session()
        self.loginName = '账号'
        self.password = '密码'
        # self.down_url = 'http://videotts.it211.com.cn/'
        self.down_url = 'http://c.it211.com.cn/'
        # self.path = 'D:/download/'
        self.path = './download/'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'http://www.tmooc.cn/',
        }

    def login(self):
        self.session.get('http://uc.tmooc.cn/userValidata/getUserInfo')
        data = {
            'loginName': self.loginName,
            'password': hashlib.md5(self.password.encode(encoding='UTF-8')).hexdigest(),
            'accountType': '1'
        }
        self.session.post('http://uc.tmooc.cn/login', data=data)
        requests.utils.add_dict_to_cookiejar(self.session.cookies, {'isCenterCookie': 'yes'})
        self.session.get('http://tts.tmooc.cn/user/myTTS',
                         params={'sessionId': self.session.cookies.get_dict()['TMOOC-SESSION']})
        try:
            self.session.cookies.get_dict()['sessionid']
            print('登录成功')
            return True
        except:
            print('登录失败')
            return False

    def get_tts(self):
        res = self.session.get('http://tts.tmooc.cn/studentCenter/toMyttsPage', headers=self.header)
        # html = etree.HTML(res.text)
        # return {key: [i for i in val.xpath('./li/ul/li[@class="sp"]/a/@href')] for key, val in zip(html.xpath('/html/body/div[2]/div/div/div[1]/h2/span/text()'), html.xpath('/html/body/div[2]/div/div/div[1]/div/div/ul'))}
        soup = BeautifulSoup(res.text, 'lxml')
        return {key.span.string: [i.find('li', 'sp').a['href'] for i in val.find_all('li', 'opened')] for key, val in
                zip(soup.find_all('h2', 'headline-1'), soup.find_all('div', 'course-list'))}

    def get_video(self, url):
        print(url)
        res = self.session.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        result = soup.find('div', 'video-list')('p')
        try:
            ret = [(i.a['title'], i.a['onclick'][13:-12]) for i in result]
            return ret
        except:
            print('视频未绑定:', url)
            return False

    def download(self, url):
        res = self.session.get(url, headers=self.header)
        if res.status_code == requests.codes.ok:
            return res
        else:
            print(url, res.status_code)
            return False


class M3u8:
    def __init__(self, m3u8):
        self.m3u8 = m3u8

    def find_key(self):
        pattern = re.compile(r'#EXT-X-KEY:.+')
        result = pattern.findall(self.m3u8)
        if result:
            result = result[0].replace('#EXT-X-KEY:', '').split(',')
            return {i.split('=')[0]: i.split('=')[1].strip('"') if i.split('=')[0] == 'URI' else i.split('=')[1] for i
                    in result}

    def find_ts(self):
        # pattern = re.compile(r'#EXTINF:.+\n.+')
        pattern = re.compile(r'http://.+\.ts')
        result = pattern.findall(self.m3u8)
        if result:
            return [i for i in result]

    def aes_decode(self, file, key=None):
        if key:
            return AES.new(key, AES.MODE_CBC, key).decrypt(file)
        return file


def m3u8_download(url, path, tedu):
    m3m8_res = tedu.download(url)
    if m3m8_res:
        m3u8 = M3u8(m3m8_res.text)
        key_res = tedu.download(m3u8.find_key()['URI'])
        if key_res:
            key = key_res.content
            for ts in m3u8.find_ts():
                print(ts)
                ts_res = tedu.download(ts)
                if ts_res:
                    ts_file = ts_res.content
                    try:
                        with open(path + '.mp4', 'ab', buffering=0) as f:
                            f.write(m3u8.aes_decode(ts_file, key))
                    except:
                        print('写文件出错')


def main():
    tedu = Tedu()
    if tedu.login():
        tts_dic = tedu.get_tts()
        f_list = list(tts_dic.keys())
        print(f_list)
        # 阶段
        for f in f_list:
            path = tedu.path + str(f_list.index(f) + 1) + '_' + f
            # print(path)
            if not os.path.exists(path):
                os.makedirs(path)
            # 天
            for url in tts_dic[f]:
                file_path = path + '/' + str(tts_dic[f].index(url) + 1) + '.'
                print(file_path)
                video_list = tedu.get_video(url)
                # 章节
                if video_list:
                    for v in video_list:
                        print(v)
                        file_name_path = file_path + str(video_list.index(v) + 1) + '_' + v[0]
                        m3u8_url = tedu.down_url + v[1] + '/' + v[1] + '.m3u8'
                        m3u8_download(m3u8_url, file_name_path, tedu)


if __name__ == "__main__":
    main()
