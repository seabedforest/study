"""
v 视图展示,发送请求,接收结果展示
"""
from socket import *
import sys

# 服务器地址
ADDR = ("127.0.0.1", 8888)


# 二级界面
def login_mean(sockfd, name):
    while True:
        print("""
           ==================Welcome===================
           1.查单词           2.查历史记录          3.注销
           """)
        cmd = input("请输入选项")
        if cmd == '1':
            do_query(sockfd, name)
        elif cmd == '2':
            do_history(sockfd,name)
        elif cmd == '3':
            return
        else:
            print("请输入正确的选项")


# 客户端注册
def do_register(sockfd):
    while True:
        name = input("请输入你的姓名:")
        passwd = input("请输入密码:")
        if " " in name or " " in passwd:
            print("用户名或密码不能包含空格")
            continue
        message = "R %s %s" % (name, passwd)
        sockfd.send(message.encode())
        # 等待结果
        result = sockfd.recv(128).decode()
        if result == "YES":
            print("注册成功")
            login_mean(sockfd, name)
        else:
            print("注册失败")
        return


# 请求登录
def do_login(sockfd):
    while True:
        name = input("请输入你的姓名:")
        passwd = input("请输入密码:")
        message = "L %s %s" % (name, passwd)
        sockfd.send(message.encode())  # 发送登录请求
        # 等待结果
        result = sockfd.recv(128).decode()
        if result == "YES":
            print("登录成功")
            login_mean(sockfd, name)
        else:
            print("登录失败")
        return


# 查询操作
def do_query(sockfd, name):
    while True:
        word = input("单词:")
        if word == "##":
            break
        msg = "Q %s %s" % (name, word)
        sockfd.send(msg.encode())
        data = sockfd.recv(2048).decode()
        print(data)


# 历史记录
def do_history(sockfd, name):
    msg = "H " + name
    sockfd.send(msg.encode())
    while True:
        # 每次接收一个历史记录
        data = sockfd.recv(1024).decode()
        if data == "##":
            break
        print(data)


def main():
    try:
        sockfd = socket()
        sockfd.connect(ADDR)
    except:
        print("请检查你的网络后重试! ")
        return
        # sys.exit("客户端退出")

    # 进入一级界面
    while True:
        print("""
           ==================Welcome===================
           1.注册             2.登录               3.退出
           """)
        cmd = input("请输入选项")
        if cmd == '1':
            do_register(sockfd)
        elif cmd == '2':
            do_login(sockfd)
        elif cmd == '3':
            sockfd.send(b'E')
            sys.exit("谢谢使用")
        else:
            print("请输入正确的选项")


if __name__ == '__main__':
    main()
