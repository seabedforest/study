import time

time.time()


# 间隔 = 执行后 - 执行前
def gain_time(func):
    start_time = time.time()
    def wrapper(*args, **kwargs):
        end_time = time.time()
        interval_time = end_time - start_time
        print(interval_time,"miao")
        return func(*args, **kwargs)
    return wrapper

@gain_time
def func01(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(func01(10))
print(func01(1000))
