from socket import *

# 创建tcp套接字
tcp_socket = socket()

# 发起连接
tcp_socket.connect(("127.0.0.1",8888))

filename = input("File:")
f = open(filename,'rb') # 打开文件

# 读取文件内容，发送给服务端
while True:
    data = f.read(1024 * 10)
    if not data:
        break
    tcp_socket.send(data)

# 关闭套接字
f.close()
tcp_socket.close()