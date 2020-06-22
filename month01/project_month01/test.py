"""
小明家必须要过一座桥。小明过桥最快要１秒，小明的弟弟最快要３秒，小明的爸爸最快要６秒，小明的妈妈最快要８秒，
小明的爷爷最快要１２秒。每次此桥最多可过两人，而过桥的速度依过桥最慢者而定。过桥时候是黑夜，所以必须有手电筒，
小明家只有一个手电筒，而且手电筒的电池只剩30秒就将耗尽。小明一家该如何过桥，请写出详细过程。
@author hailin
@date 2020-06-04
"""
import itertools

# import random

"""
解题思路：
如何在30秒之内，全家都过桥。因为只有一个手电筒，所以必须有人来回传递手电筒，肯定要用过桥速度快的人来传递手电筒
耗时长的两个可以一块过桥节省时间，大概过程如下：
1.小明跟弟弟一块过桥 3秒
2.小明回来  1秒
3.妈妈跟爷爷一块过桥 12秒
4.弟弟回来  3秒
5.小明跟爸爸过桥   6秒
6.小明回来  1秒
7.小明跟弟弟一块过桥 3秒
全家过桥完毕用时为 3+1+12+3+6+1+3=29秒
"""
import itertools


def calcu_from(a, b,second=0):
    '''
    在当前 a / b 情况下，计算从 A -> B 所有可能的过河时间
    '''

    result = set()
    for step in itertools.combinations(a, 2):
        m = max(step)
        totle_time = m + second
        tmp_b = b[:]
        tmp_b.extend(step)
        next = calcu_to([e for e in a if e not in step], tmp_b)
        for n in next:
            result.add(n + m)
        print(totle_time)
    return result


def calcu_to(a, b):
    '''
    在当前 a / b 情况下，计算从 B -> A 所有可能的过河时间
    '''
    if len(a) == 0:
        return {0}

    result = set()
    m = min(b)
    tmp_a = a[:]
    tmp_a.extend([min(b)])
    next = calcu_from(tmp_a, [e for e in b if e not in [min(b)]],m)
    for n in next:
        result.add(n + m)
    return result


a = [1, 3, 6, 8, 12]
b = []

result = calcu_from(a, b)
print(result)
