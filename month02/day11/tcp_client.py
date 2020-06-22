"""
tcp套接字  客户端
"""
from socket import *

# 创建套接字
tcp_socket = socket()
# 发起连接
tcp_socket.connect(("127.0.0.1", 8090))
# 发送接收信息
msg = input(">>>")
tcp_socket.send(msg.encode())
data = tcp_socket.recv(1024)
if data:
    print("从服务器收到:", data.decode())

# 关闭
tcp_socket.close()
