"""
process 模块演示
"""
import multiprocessing

# 进程执行函数
from time import sleep
a=1

def fun01():
    print("开始运行一个进程")
    sleep(2)
    print("一个进程执行结束了")

def fun02():
    print("开始运行2进程")
    global a
    print('a:',a)
    a=100
    print('a:', a)
    sleep(3)
    print("2进程执行结束了")


if __name__ == '__main__':
    # 创建进程对象
    print("a", a)
    p = multiprocessing.Process(target=fun01)

    # 启动进程
    p.start()
    print("a", a)
    s = multiprocessing.Process(target=fun02)
    s.start()
    print("aa",a)
    s.join()

    # 回收进程
    p.join(30)
    print("aaa",a)