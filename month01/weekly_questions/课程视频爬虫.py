from time import sleep

import requests
import re

list_url = []


def get_url():
    global list_url
    link = "http://video.mobiletrain.org/course/index/courseId/495"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36"}
    r = requests.get(link, headers=headers)
    pattern = r'data-url="(.*)" class="fr">点击播放'
    count = r.text
    list_url = re.findall(pattern, count)


def save_video(url, name):
    print(name, "开始下载")
    video = requests.get(url)
    f = open(name, "ab")
    f.write(video.content)
    f.close()
    print(name, "下载完成")


if __name__ == '__main__':
    get_url()
    print(list_url)
    for item in list_url:
        index = item.rfind("com")
        name = item[index + 4:]
        save_video(item, name)
        sleep(60)
