import os
import time
from multiprocessing import Process


def fun():
    print(time.ctime())
    time.sleep(10)
    print(time.ctime())


p = Process(target=fun, name="sanlin")
p.daemon = False
p.start()
print("Name:", p.name)
print("PID:", p.pid)
print("saving", p.is_alive())
print("ppid", os.getppid())
time.sleep(20)
