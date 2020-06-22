import sys
from socket import *
from select import select

# 创建监听套接字
sockfd = socket()
sockfd.bind(("0.0.0.0", 8090))
sockfd.listen(5)

#IO多路复用配合网络时一般为非阻塞网络模型
sockfd.setblocking(False)

# 设置关注列表
rlist = [sockfd]
wlist = []
xlist = []

# 循环监控我们放入列表中的IO
#
while True:
        try:
            # 对IO进行关注
            rs, ws, xs = select(rlist, wlist, xlist)
        except KeyboardInterrupt as e:
            sockfd.close()
            sys.exit("服务器退出")
        # 对rs分情况 --> sockfd 一类: 客户端连接    connfd一类: 对应的客户端发消息
        for r in rs:
            if r is sockfd:
                connfd, addr = r.accept()
                print("Connect from ", addr)
                # 每连接一个客户端，就将这个客户端连接套接字加入关注
                connfd.setblocking(False)
                rlist.append(connfd)
            else:
                data = r.recv(1024)
                if not data:
                    # 客户端退出处理
                    rlist.remove(r)
                    r.close()
                    continue
                print(data.decode())
                wlist.append(r)
        for w in ws:
            w.send(b"OK")
            wlist.remove(w)

        for x in xs:
            pass

