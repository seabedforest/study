"""
进程池
"""
from multiprocessing import Pool
from time import ctime, sleep
import random


def worker(msg, sec):
    print(ctime(), '--------', msg)
    sleep(sec)


# 创建进程池
pool = Pool(10)

# 向进程池事件队列加入事件

for i in range(10):
    msg = "Tedu-%d" % i
    pool.apply_async(func=worker, args=(msg, random.randint(1, 5)))

# 关闭进程池
pool.close()

# 阻塞等待回收进程池中的进程
pool.join()
