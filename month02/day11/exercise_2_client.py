
from socket import *

# 创建tcp套接字
tcp_socket = socket()

# 发起连接
tcp_socket.connect(("127.0.0.1",8888))

while True:
    # 发送接收消息
    msg = input("我：")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("小美:",data.decode())

# 关闭套接字
tcp_socket.close()