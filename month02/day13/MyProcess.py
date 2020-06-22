from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, value):
        self.value = value
        super().__init__()

    # 复杂事件处理
    def fun1(self):
        print("步骤1：假设很复杂")

    def fun2(self):
        print("步骤2：假设很复杂2")

    # 重写进程开启
    def run(self):
        self.fun1()
        self.fun2()


p = MyProcess(1)
p.start()
p.join()
