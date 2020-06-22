"""
http请求
"""
from socket import *

s = socket()
s.bind(('0.0.0.0', 8090))
s.listen(5)

c, addr = s.accept()
print("Connect from", addr)

data = c.recv(4096)  # 接收到浏览器的请求内容
print(data.decode())

# 发送给浏览器一些内容,让其显示
# 按照响应格式组织
response = "HTTP/1.1 200 OK\r\n"
response += "Content-Type:text/html\r\n"
response += "\r\n"
with open("myweb.html") as f:
    response += f.read()

print(response)
c.send(response.encode())

# 关闭
c.close()
s.close()
