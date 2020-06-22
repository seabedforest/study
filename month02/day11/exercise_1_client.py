from socket import *

# 访问服务器的地址
ADDR = ('172.40.91.178',8888)

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 循环发送接收消息
while True:
    # 发送单词
    word = input("Word:")
    # 结束循环
    if not word:
        break
    udp_socket.sendto(word.encode(),ADDR)
    # 接收单词解释 data
    data,addr = udp_socket.recvfrom(1024)
    print("%s : %s"%(word,data.decode()))

# 关闭套接字
udp_socket.close()