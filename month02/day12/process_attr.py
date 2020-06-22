"""
进程对象属性
"""

from multiprocessing import Process
import time
import os,sys

def fun():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)


# 创建进程对象
p = Process(target=fun,name="Tarena")

# 该子进程会随父进程的退出而结束
p.daemon = True

p.start()

print("Name:",p.name)
print("PID:",p.pid)
print("is alive:",p.is_alive())

