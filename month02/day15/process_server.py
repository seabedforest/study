"""
多进程tcp并发模型
"""
import sys
from socket import *
from multiprocessing import Process
from signal import *

# 全局变量
HOST = "0.0.0.0"
PORT = 8090
ADDR = (HOST, PORT)


# 处理客户端请求
def handle(connfd):
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print("客户端:", data)
        connfd.send(b"ok")
    connfd.close()


def main():
    # tcp套接字
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(ADDR)
    s.listen(3)
    print("Listen the port %d..." % PORT)

    # 处理子进程
    signal(SIGCHLD, SIG_IGN)
    # 循环连接客户端
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt as e:
            s.close()
            sys.exit("该服务器已经退出")

        # 创建子进程处理客户端具体请求事务
        p = Process(target=handle, args=(c,))
        p.daemon = True  # 如果父进程退出，所有服务立即终止则可以使用
        p.start()


if __name__ == '__main__':
    main()
