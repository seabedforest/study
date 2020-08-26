"""
递归 打印1+2+3+...+n的和
"""


def sumn(n):
    if n == 1:
        return 1
    return n + sumn(n - 1)


print(sumn(4))

"""
计算n的阶乘： 5*4*3*2*1=120
"""


def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)


print(f(5))
