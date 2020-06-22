"""
小梅机器人上线了
"""
from socket import *
#创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)
#绑定地址
tcp_socket.bind(('0.0.0.0',8090))
#设置监听
tcp_socket.listen(3)
dict01={"你多大了":"2岁了","男的还是女的":"人家女孩子","哦哦":"哦你个头",}
#收发消息
while True:
    # 等待客户端连接（阻塞函数)
    print("waitiog for connect....")
    connfd, addr = tcp_socket.accept()
    print("connect from:", addr)
    while True:
        data = connfd.recv(1024)
        if data.decode() in dict01:
            connfd.send(dict01[data.decode()].encode())
        elif data == b"##":
            connfd.close()
            break
        else:
            connfd.send("你说的是什么啊我不懂".encode())


#关闭
tcp_socket.close()