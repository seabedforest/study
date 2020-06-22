"""
chat room 客户端
发送请求，获取结果
"""
from socket import *
from multiprocessing import Process

ADDR = ('127.0.0.1', 8090)


def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(4096)
        print(data.decode())


# 进入聊天室
def login(sock):
    while True:
        name = input("Name:")
        msg = "L " + name  # 根据通信协议做标志 L 登录
        sock.sendto(msg.encode(), ADDR)
        result, addr = sock.recvfrom(128)
        if result.decode() == "OK":
            print("进入聊天室")
            return name
        else:
            print("该用户已存在")


def chat(sock, name):
    while True:
        message = input(">>>")
        msg = "C %s %s" % (name, message)
        sock.sendto(msg.encode(), ADDR)
        result, addr = sock.recvfrom(1024)
        if result.decode() == "quit":
            print("退出聊天室")
            return
        else:
            print(result)


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    name = login(sock)
    # 创建子进程
    p = Process(target=recv_msg, args=(sock,))
    p.start()
    chat(sock, name)
    p.join()


if __name__ == '__main__':
    main()
