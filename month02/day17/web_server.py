"""
web server 程序

IO多路复用和http训练
"""
import re
import sys
from socket import *
from select import select
from multiprocessing import Process


class WebServer:
    def __init__(self, host="0.0.0.0", port=8000, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.address = (host, port)
        self.create_socket()
        self.bind()
        self._rlist = []
        self._wlist = []
        self._xlist = []

    # 启动 web服务
    def start(self):
        self.sock.listen(5)
        print("Listen to the port %d" % self.port)
        self._rlist.append(self.sock)
        while True:
            try:
                rs, ws, xs = select(self._rlist, self._wlist, self._xlist)
            except KeyboardInterrupt as e:
                self.sock.close()
                sys.exit("Web服务已经退出")
            for r in rs:
                if r is self.sock:
                    # 有浏览器连接
                    connfd, addr = r.accept()
                    # print("Connect from ", addr)
                    connfd.setblocking(False)
                    self._rlist.append(connfd)
                else:
                    try:
                        self.handle(r)
                    except:
                        r.close()
                        self._rlist.remove(r)

    # 创建套接字
    def create_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.sock.bind(self.address)

    def handle(self, connfd):
        request = connfd.recv(4096).decode()
        # 解析请求 --> 解析出请求内容 请求行的第二部分
        pattern = "[A-Z]+\s+(?P<info>/\S*)"
        result = re.match(pattern, request)
        if result:
            info = result.group("info")
            print("请求内容: ", info)
            self.get_html(connfd, info)  # 判定网页是否存在，给客户端响应
        else:
            connfd.close()
            self._rlist.remove(connfd)
            return

    # 组织数据给客户端回复
    def get_html(self, connfd, info):
        if info == "/":
            filename = self.html + "/index.html"
        else:
            filename = self.html + info

        try:
            fd = open(filename, 'rb')
        except:
            response = "HTTP/1.1 404 Not Fount\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry...Not Fount</h1>"
            response = response.encode()
        else:
            data = fd.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "Content-Length:%d\r\n" % len(data)
            response += "\r\n"
            response = response.encode() + data
            fd.close()
        finally:
            connfd.send(response)


if __name__ == '__main__':
    httpd = WebServer(host='0.0.0.0', port=8000, html="./static")
    httpd.start()
