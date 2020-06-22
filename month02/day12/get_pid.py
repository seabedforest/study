"""
进程相关函数演示
创建多个子进程
"""

from multiprocessing import Process
from time import sleep
import os,sys

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),"---",os.getpid())

def th2():
    sleep(2)
    sys.exit("睡觉进程退出") # 结束进程
    print("睡觉")
    print(os.getppid(),"---",os.getpid())

def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(),"---",os.getpid())

things = [th1,th2,th3]
jobs = []
# 每次循环创建一个进程
for th in things:
    p = Process(target=th)
    jobs.append(p) # 将三个进程对象都放入列表
    p.start()

# 统一回收
for i in jobs:
    i.join()




