"""
select IO多路复用
"""
from select import select
from socket import *
from time import sleep

tcp_sock = socket()
tcp_sock.bind(('0.0.0.0', 8888))
tcp_sock.listen()

udp_sock = socket(AF_INET, SOCK_DGRAM)
udp_sock.bind(('0.0.0.0', 9999))

f = open("test.txt")

print("开始对IO进行监控")
rs, ws, xs = select([tcp_sock, f], [], [])
print("rlist:", rs)
print("wlist:", ws)
print("xlist:", xs)
