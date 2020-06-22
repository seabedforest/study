import sys
from socket import *
from select import *

# 创建监听套接字
sockfd = socket()
sockfd.bind(("0.0.0.0", 8090))
sockfd.listen(5)

# IO多路复用配合网络时一般为非阻塞网络模型
sockfd.setblocking(False)
# 创建poll对象
p = poll()

# 建立查找字典
map = dict({})

# 设置IO关注 读事件
p.register(sockfd, POLLIN)
map[sockfd.fileno()] = sockfd
# 循环监控,等待IO事件发生
try:
    while True:
        events = p.poll()
        # 循环遍历events 分情况讨论处理
        for fd, event in events:
            # fd --就绪IO文件描述符   event--> 就绪io就绪什么事件类型
            if fd == sockfd.fileno():
                connfd, addr = map[fd].accept()
                print("Connect from ", addr)
                # 每连接一个客户端，就将这个客户端连接套接字加入关注
                connfd.setblocking(False)
                p.register(connfd, POLLIN)
                map[connfd.fileno()] = connfd  # 查找字典时刻与监听的IO保持一致
            else:
                data = map[fd].recv(1024)
                if not data:
                    p.unregister(fd)
                    map[fd].close()
                    del map[fd]
                    continue
                print(data.decode())
                map[fd].send(b'OK')

except KeyboardInterrupt as e:
    sockfd.close()
    sys.exit("服务器退出")