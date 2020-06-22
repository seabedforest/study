"""
@author hailin
@date 2020-06-13
env: python 3.6
socket and Process exercise
"""

from socket import *

# 服务器地址
HOST = "0.0.0.0"
PORT = 8090
ADDR = (HOST, PORT)

# 存储用户字典
user = {}


def do_login(sock, name, address):
    if name in user:
        sock.sendto(b"Fail", address)
        return
    else:
        sock.sendto(b"OK", address)
        # 通知其他人
        msg = "欢迎 %s 进入聊天室" % name
        for i in user:
            sock.sendto(msg.encode(), user[i])
        # 存储用户
        user[name] = address
        # print(user)


def transpond(sock, name, message):
    msg = "%s : %s" % (name, message)
    for i in user:
        if i != name:
            sock.sendto(msg.encode(), user[i])


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)
    # 循环接收用户的请求
    while True:
        # 接收用户的请求(所有的客户端所有的请求都在这里接收)
        data, addr = sock.recvfrom(1024)
        tmp = data.decode().split(' ', 2)
        # 根据请求调用模块
        if tmp[0] == 'L':
            do_login(sock, tmp[1], addr)
        elif tmp[0] == 'C':
            transpond(sock, tmp[1], tmp[2])


if __name__ == '__main__':
    main()
