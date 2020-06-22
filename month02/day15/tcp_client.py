"""
单一tcp客户端循环发送内容
"""
from socket import *

# 创建tcp套接字
tcp_sock = socket(AF_INET, SOCK_STREAM)
tcp_sock.connect(("127.0.0.1",8090))
while True:
    msg = input(">>>")
    if not msg:
        break
    tcp_sock.send(msg.encode())
    data = tcp_sock.recv(1024)
    print("从服务器收到:",data.decode())

tcp_sock.close()