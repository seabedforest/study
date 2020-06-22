"""
tcp服务端，循环接收一个客户端的消息
一个客户端退出在接收下一个客户端
重点代码
"""

from socket import *

# 创建TCP套接字 （不写参数默认也是tcp）
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(('0.0.0.0',8888))

# 设置监听
tcp_socket.listen(3)

while True:
    # 等待客户端连接 (阻塞函数)
    print("Waiting for connect ....")
    connfd,addr = tcp_socket.accept()
    print("Connect from",addr)

    # 循环接收来自某一个客户端的消息
    while True:
        # 收发消息
        data = connfd.recv(1024)
        # 服务端退出方法1 data为空字节串那么表示另外一侧已经退出
        # if not data:
        #     break

        # 第二种服务端退出方法，收到特殊字符退出
        if data == b'##':
            break
        print("收到:",data.decode())

        connfd.send(b"Thanks#")

    connfd.close()

# 关闭
tcp_socket.close()