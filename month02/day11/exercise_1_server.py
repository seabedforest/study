"""
客户端可以循环输入单词，得到单词的解释

* 单词使用数据库查询 dict
* 数据库与服务端程序在一起的

思路 :  客户端 --》 发送给服务端 --》服务端通过数据库查询 -》将解释发送个客户端展示
"""

from socket import *
import pymysql

class Database:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="123456",
                             database="dict",
                             charset="utf8")
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    # 查找单词方法
    def find_word(self,word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql,[word])
        result = self.cur.fetchone() # (mean,)  None
        if result:
            return result[0]
        else:
            return "Not Found"

def main():
    # 创建udp套接字
    sockfd = socket(AF_INET,SOCK_DGRAM)
    sockfd.bind(("0.0.0.0",8888))
    db = Database() # 实例化对象
    while True:
        # 接收单词
        word,addr = sockfd.recvfrom(50)
        mean = db.find_word(word.decode())
        # 发送给客户端解释
        sockfd.sendto(mean.encode(),addr)
    db.close()
    sockfd.close()

if __name__ == '__main__':
    main()