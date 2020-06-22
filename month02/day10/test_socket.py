"""
套接字函数实例
"""
import socket
#创建udp连接
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定IP地址和端口
udp_socket.bind(("localhost",8090))
