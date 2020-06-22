"""
输入一个正数n，输出所有和为n 连续正数序列。
例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以输出3 个连续序列1-5、4-6 和7-8。
@author hailin
@date 2020-06-18
"""


def get_longest_sequence(n):
    """
    获取正数n的最长连续正数序列(从1开始,输出所有和为n)
    :param n: 正数n
    :return: 最长连续正数序列
    """
    seq = []
    m = 0
    for i in range(1, n // 2 + 1):
        m += i
        if m <= n:
            seq.append(i)

    return seq


def get_sequence(n):
    """
    打印出多个连续序列的结果
    :param n:正数n
    :return:None
    """
    seq = get_longest_sequence(n)
    print("%d-%d" % (min(seq), max(seq)))
    begin = max(seq)
    end = n // 2 + 1

    for i in range(begin + 1, end + 1):
        seq.append(i)
        while sum(seq) > n:
            seq.pop(0)
            if sum(seq) == n:
                print("%d-%d" % (min(seq), max(seq)))


get_sequence(15)


def get_num_seq(n):
    """
    一个正数n，输出所有和为n 连续正数序列
    :param n: 正数n>
    :return: None
    """
    for i in range(1, n // 2 + 2):  # 外循环控制循环次数
        total = 0
        seq = []
        for j in range(i, n // 2 + 2):  # 计算和为n 连续正数序列
            total += j
            seq.append(j)
            if total == n:
                print("%d-%d" % (min(seq), max(seq)))
                break


get_num_seq(15)
