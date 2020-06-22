"""
Process 模块创建进程演示
1.将需要新进程执行的事件封装为函数
2.通过模块的Process类创建进程对象，关联函数
3.通过进程对象调用start启动进程
4.通过进程对象调用join回收进程资源
"""

import multiprocessing
from time import sleep

a = 1

# 进程执行函数
def fun():
    print("开始运行一个进程")
    global a
    print("a =",a)
    a = 1000
    sleep(2)
    print("一个进程执行结束了")

# 创建进程对象
p = multiprocessing.Process(target=fun)

# 启动进程  进程诞生， 自动的运行fun 将其作为新进程的执行内容
p.start()

print("原进程干点事")
sleep(3)
print("父进程干完了")

# 回收进程 阻塞等待新进程结束
p.join()

print("a:",a)



