"""
练习2: tcp上传头像　
将一张图片，从客户端发送到服务端（服务端以当前日期命名）　
支持ｊｐｇ　ｐｎｇ　　ｊｐｅｇ格式上传

思路：　客户端　－－》　读取文件　发送
　　　　服务端　－－》　接收　　写入文件
"""

from socket import *
from time import localtime

# 创建TCP套接字
tcp_socket = socket()
tcp_socket.bind(('0.0.0.0', 8888))
tcp_socket.listen(3)

# 等待客户端连接 (阻塞函数)
print("Waiting for connect ....")
connfd, addr = tcp_socket.accept()
print("Connect from", addr)

# 打开文件
filename = "%d-%d-%d.jpg" % localtime()[:3]
f = open(filename, 'wb')

# 收发文件内容写入本地
while True:
    data = connfd.recv(1024 * 10)
    if not data:
        break
    f.write(data)

# 关闭
f.close()
connfd.close()
tcp_socket.close()
