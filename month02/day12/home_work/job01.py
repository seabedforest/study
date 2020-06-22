"""
编写一个函数求100000以内质数之合 --》 统计函数执行时间（装饰器）
@author hailin
@date 2020-06-12
"""
import time


def execution_time(fun):
    def parcel(*args, **kwargs):
        start_time = time.time()
        result = fun(*args, **kwargs)
        end_time = time.time()
        totle_time = end_time - start_time
        print("所使用的时间:", totle_time)
        return result

    return parcel


@execution_time
def get_prime_number():
    prime_number_total = 0
    for i in range(2, 100001):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_number_total += i


get_prime_number()
# "所使用的时间:34.088390588760376"
