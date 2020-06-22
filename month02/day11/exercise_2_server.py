"""
练习1 ：  完成一个简单的 模拟机器人客服对话程序

小美    你多大了？  ————》 我2对啦
       你男生女生 ---》 人家女孩子啦
       xxxx  ---> xxxxx

在客户端输入问题，得到回答
"""

from socket import *

# 对话字典
chat = {
    "你好":"你好",
    "叫什么":"我叫小美啊",
    "男的女的":"人家女孩子啦",
    "几岁":"我2岁啦",
    "我美":"你是个漂亮的女孩子"
}


# 创建TCP套接字
tcp_socket = socket()
tcp_socket.bind(('0.0.0.0',8888))
tcp_socket.listen(3)

while True:
    # 等待客户端连接 (阻塞函数)
    print("Waiting for connect ....")

    try:
        connfd,addr = tcp_socket.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        break

    # 循环接收来自某一个客户端的消息
    while True:
        # 收发消息 人类的问题
        data = connfd.recv(1024)
        if not data:
            break
        # 遍历字典 (key)
        for i in chat:
            if i in data.decode():
                connfd.send(chat[i].encode())
                break
        else:
            connfd.send("人家还小，听不懂".encode())

    connfd.close()

# 关闭
tcp_socket.close()