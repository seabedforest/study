"""
tcp 服务器
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 绑定地址
tcp_socket.bind(('0.0.0.0', 8090))
# 设置监听
tcp_socket.listen(3)
# 等待客户端连接（阻塞函数)
print("waitiog for connect....")
connfd, addr = tcp_socket.accept()
print("connect from:", addr)
# 收发消息
data = connfd.recv(1024)
if data:
    print("收到:", data.decode())

# 回复
connfd.send("Thanks".encode())
# 关闭
connfd.close()
tcp_socket.close()
