from select import *
from socket import *
from time import sleep

tcp_sock = socket()
tcp_sock.bind(("0.0.0.0", 8090))
tcp_sock.listen()

udp_sock = socket(AF_INET, SOCK_DGRAM)
udp_sock.bind(("0.0.0.0", 8888))

f = open("test.txt")

p = poll()  # poll对象
p.register(tcp_sock, POLLIN) # 关注IO

p.register(f, POLLIN)
print(tcp_sock.fileno(), POLLIN)
sleep(2)

print(f.fileno(),POLLIN)
events = p.poll()
print(events)
