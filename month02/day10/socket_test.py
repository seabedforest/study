"""
套接字基础函数示例
"""
import socket

# 创建一个udp套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 客户端只能与服务端在同一主机上，使用("127.0.0.1",8888)访问服务端
udp_socket.bind(("127.0.0.1",8888))
udp_socket.bind(("localhost",8888))

# 客户端能够在任何主机上，使用("172.40.91.178",8888)访问服务端
udp_socket.bind(("172.40.91.178",8888))

# 客户端能够在任何主机上，如果在其他主机("172.40.91.178",8888)访问服务端
# 如果与服务端在同一主机可以使用("127.0.0.1",8888)或者("172.40.91.178",8888)
udp_socket.bind(("0.0.0.0",8888))
udp_socket.bind(("",8888))