"""
创建线程示例2
"""
from threading import Thread
from time import sleep


# 含有参数的线程函数
def fun(sec, name):
    sleep(sec)
    print("%s含有参数的线程" % name)
    sleep(sec)
    print("%s线程执行完毕" % name)


# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun, args=(2,), kwargs={"name": 'T%d' % i})
    jobs.append(t)
    t.start()
    print(t.getName())
# 回收线程
[i.join() for i in jobs]
