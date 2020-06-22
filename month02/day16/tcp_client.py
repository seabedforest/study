"""
tcp套接字  客户端
"""
from socket import *

# 创建套接字
sockfd = socket()
# 发起连接
sockfd.connect(("127.0.0.1", 8090))
# 发送 接收信息
while True:
    msg = input(">>>")
    if not msg:
        break
    sockfd.send(msg.encode())
    data = sockfd.recv(1024).decode()
    print(data)

# 关闭
sockfd.close()
