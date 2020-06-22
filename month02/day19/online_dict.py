"""
c 逻辑控制,基础结构搭建,接受请求,调用数据,数据整合提供给客户端
"""
from multiprocessing import Process
from socket import *
import signal, sys, time
from dict_db import DataBase

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

# 实例化数据库对象
db = DataBase()


# 处理注册
def do_register(connfd, name, passwd):
    # 判断可否注册--> 数据库处理-->调用数据库方法解决问题
    # 返回True 表示可以注册 False 表示注册不成功
    if db.register(name, passwd):
        connfd.send(b"YES")
    else:
        connfd.send(b"NO")


# 登录处理
def do_login(connfd, name, passwd):
    if db.login(name, passwd):
        connfd.send(b"YES")
    else:
        connfd.send(b"NO")


# 单词查询
def do_query(connfd, name, word):
    # 插入历史记录
    db.insert_history(name, word)

    # 查询单词
    mean = db.query(word)
    # 根据查询情况分情况处理 True 解释 False None
    if mean:
        data = "%s : %s" % (word, mean)
    else:
        data = "%s : Not Found" % word
    connfd.send(data.encode())


# 历史记录
def do_history(connfd, name):
    data = db.history(name)
    # data --> ((name,history,times),(),..)
    for i in data:
        # i --> (name,history,times)
        msg = "%-10s    %-10s   %-s" % i
        connfd.send(msg.encode())
        time.sleep(0.1)
    connfd.send(b"##")


# 处理客户端请求的过程
def handle(connfd):
    db.cursor()  # 每个子进程创建自己的游标
    # 接收某一个客户端的各种请求
    while True:
        data = connfd.recv(1024).decode()
        if not data or data == b'E':
            # 客户端结束
            break
        msg = data.split(' ')
        if msg[0] == 'R':
            # msg -->[R name passwd]
            do_register(connfd, msg[1], msg[2])
        elif msg[0] == 'L':
            # msg -->[L name passwd]
            do_login(connfd, msg[1], msg[2])
        elif msg[0] == 'Q':
            # msg -->[Q name word]
            do_query(connfd, msg[1], msg[2])
        elif msg[0] == 'H':
            # msg -->[H name]
            do_history(connfd, msg[1])

    # 关闭子进程对应的资源
    connfd.close()
    db.cur.close()


# 网络并发模型
def main():
    # 创建套接字
    sockfd = socket()
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print("Listen the port %d" % PORT)
    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    # 循环等待客户端连接
    while True:
        try:
            connfd, addr = sockfd.accept()
            print("Connect from ", addr)
        except KeyboardInterrupt:
            db.close()
            sockfd.close()
            sys.exit("服务端退出")

        # 客户端连接则创建进程
        p = Process(target=handle, args=(connfd,))
        p.daemon = True
        p.start()


if __name__ == '__main__':
    main()
