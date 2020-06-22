"""
使用udp套接字完成
客户端可以循环输入单词，得到单词的解释
* 单词使用数据库查询 dict
* 数据库与服务端程序在一起的
"""
from socket import *
import pymysql


# 连接数据库
def connect_mysql(word):
    db = pymysql.connect(host="localhost",
                         port=3306,
                         user="root",
                         password="123456",
                         database="dict",
                         charset="utf8")
    cur = db.cursor()
    sql = "select mean from words where word=%s;"
    cur.execute(sql, [word])
    mean = cur.fetchone()
    cur.close()
    db.close()
    if not mean:
        return "查询不到该单词"
    return ''.join(mean)


# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
sockfd.bind(("176.140.11.234", 8090))

# 接收信息
while True:
    data, addr = sockfd.recvfrom(1000)
    mean = connect_mysql(data.decode())
    # 发送信息
    sockfd.sendto(mean.encode(), addr)
