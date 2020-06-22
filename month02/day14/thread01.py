"""
创建线程示例
"""
import os
import threading
from time import sleep

a = 1


# 线程执行函数
def music():
    for i in range(3):
        sleep(3)
        print(t.getName(), t.isDaemon(), "播放: 青藏高原")
        global a
        a = 1000


# 创建线程对象
t = threading.Thread(target=music)
t.setName("hai")
# 启动线程
t.start()
# 关闭线程
for i in range(3):
    sleep(2.5)
    print(os.getpid(), i)
t.join()

print(a)
