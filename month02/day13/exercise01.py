"""

"""
import time

from multiprocessing import Process


def execution_time(fun):
    def parcel(*args, **kwargs):
        start_time = time.time()
        result = fun(*args, **kwargs)
        end_time = time.time()
        totle_time = end_time - start_time
        print("所使用的时间:", totle_time)
        return result

    return parcel


class MyProcess(Process):
    def __init__(self, begin: int, end: int):
        self.begin = begin
        self.end = end
        super().__init__()

    def get_prime_number(self):
        prime_number_total = 0
        for i in range(self.begin, self.end):
            for j in range(self.begin, i):
                if i % j == 0:
                    break
            else:
                prime_number_total += i
        print(prime_number_total)

    # 求从begin 到 end 之间的质数之和
    def run(self):
        self.get_prime_number()


@execution_time
def process_4():
    jobs = []
    for i in range(2, 100001, 25000):
        p = MyProcess(i, i + 25000)
        p.start()
        jobs.append(p)

    for i in jobs:
        i.join()


process_4()
