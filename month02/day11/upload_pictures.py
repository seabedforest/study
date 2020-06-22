"""
图片上传客户端
"""
from socket import *
#创建套接字
tcp_socket=socket()
#发起连接
tcp_socket.connect(("127.0.0.1",8090))
#发送接收信息
file = input("pictures_path:")
f=open(file,"rb")
for line in f:
    tcp_socket.send(line)
else:
    f.close()

#关闭
tcp_socket.close()