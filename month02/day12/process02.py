"""
包含参数的进程函数
"""
from multiprocessing import Process
from time import sleep


def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working....")


# 位置传参
name = input("name>>")
# p=Process(target=worker,args=(2,"tom"))
# p=Process(target=worker,kwargs={"name":"lily","sec":2})
p = Process(target=worker, args=(2,), kwargs={"name": f"{name}"})
p.start()
p.join(3)
print("==================================")
