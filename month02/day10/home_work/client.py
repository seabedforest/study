"""
udp套接字客户端
"""
from socket import *

#创建套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

#发送信息
while True:
    mean=input("单词查询或退出quit>>>")
    if mean=="quit":
        break
    udp_socket.sendto(mean.encode(),("176.140.11.234",8090))
    # 接收信息
    data, addr = udp_socket.recvfrom(1000)
    print(data.decode())


udp_socket.close()