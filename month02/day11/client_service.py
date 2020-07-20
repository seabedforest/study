"""
机器人对答
"""
from socket import *

# 创建套接字
tcp_socket = socket()
# 发起连接
tcp_socket.connect(("127.0.0.1", 8888))
# 发送接收信息
while True:
    msg = input("我:")
    if msg == "##":
        tcp_socket.send(b"##")
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("小梅:", data.decode())

# 关闭
tcp_socket.close()
