"""
udp套接字服务端
"""
from socket import *

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
sockfd.bind(("176.140.11.234",8090))

#接收信息
while True:
    data,addr=sockfd.recvfrom(1000)
    print(addr[0],data.decode())
    #发送信息
    mean=input(">>>")
    sockfd.sendto(mean.encode(),addr)


#sockfd.close()