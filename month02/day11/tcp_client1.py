"""
单一tcp客户端循环发送内容
重点代码
"""

from socket import *

# 创建tcp套接字
tcp_socket = socket()

# 发起连接
tcp_socket.connect(("127.0.0.1",8888))

while True:
    # 发送接收消息
    msg = input(">>")
    # msg是空字符串则客户单退出
    if not msg:
        tcp_socket.send(b"##") # 第二中服务端退出方法，发送通知
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("从服务器收到:",data.decode())

# 关闭套接字
tcp_socket.close()