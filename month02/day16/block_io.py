"""
非阻塞io
"""
from socket import *
import time

HOST = "0.0.0.0"
PORT = 8090
ADDR = (HOST, PORT)

sockfd = socket()
sockfd.bind(ADDR)
sockfd.listen(3)

# 设置套接字sockfd 非阻塞io
# sockfd.setblocking(False)

# 设置超时时间
sockfd.settimeout(3)
while True:
    try:
        print("waiting for connect")
        connfd, addr = sockfd.accept()
        print("Connect from", addr)
    except BlockingIOError as e:
        time.sleep(2)
        with open("test.txt", 'a') as f:
            msg = "%s: %s\n" % (time.ctime(), e)
            f.write(msg)
    except timeout as e:
        with open("test.txt", 'a') as f:
            msg = "%s: %s\n" % (time.ctime(), e)
            f.write(msg)
    else:
        data = connfd.recv(1024)
        print(data.decode())
