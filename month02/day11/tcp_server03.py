"""
tcp 服务器
"""
from socket import *
#创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)
#绑定地址
tcp_socket.bind(('0.0.0.0',8090))
#设置监听
tcp_socket.listen(3)

#收发消息
while True:
    # 等待客户端连接（阻塞函数)
    print("waitiog for connect....")
    connfd, addr = tcp_socket.accept()
    print("connect from:", addr)
    while True:
        data = connfd.recv(1024)
        print("收到:",data.decode())
        if data == b"##":
            connfd.close()
            break
        #回复
        connfd.send("Thanks".encode())

#关闭
tcp_socket.close()