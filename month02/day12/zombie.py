"""
僵尸进程处理方法
"""

from multiprocessing import Process
from time import sleep
from signal import  *

# 父进程忽略子进程退出，交给系统处理
signal(SIGCHLD,SIG_IGN)

# 带参数的进程函数
def worker():
    for i in range(3):
        print("I'm Tom")
        print("I'm working...")


p = Process(target=worker)
p.start()
print(p.pid)
# p.join() # 处理僵尸

while True:
    pass
