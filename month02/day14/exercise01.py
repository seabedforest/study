"""
模拟售票系统
"""
from threading import Thread
from time import sleep

piao_list = ['T' + str(i) for i in range(1, 501)]


# print(piao_list)

def shoupiao(w):
    while piao_list:
        print("%s窗口卖出%s票" % (w, piao_list.pop(0)))
        sleep(0.1)


jobs = []
for i in range(1, 11):
    t = Thread(target=shoupiao, args=("w%d" % i,))
    jobs.append(t)
    t.start()

# 回收线程
[i.join() for i in jobs]
