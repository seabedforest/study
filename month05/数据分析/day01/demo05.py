"""
索引操作
"""
import numpy as np

a = np.arange(1, 10)
print(a)  # 1 2 3 4 5 6 7 8 9
print(a[:3])  # 1 2 3
print(a[3:6])  # 4 5 6
print(a[6:])  # 7 8 9
print(a[::-1])  # 9 8 7 6 5 4 3 2 1
print(a[:-4:-1])  # 9 8 7
print(a[-4:-7:-1])  # 6 5 4
print(a[-7::-1])  # 3 2 1
print(a[::])  # 1 2 3 4 5 6 7 8 9
print(a[:])  # 1 2 3 4 5 6 7 8 9
print(a[::3])  # 1 4 7
print(a[1::3])  # 2 5 8
print(a[2::3])  # 3 6 9

print('*' * 50)
# 高维数组的切片
a = a.reshape(3, 3)
print(a)
print('*' * 50)
print(a[:2, :2])
print('*' * 50)
print(a[::2, ::2])

# 掩码操作
a = np.arange(1, 10)
mask = [True, False, True, False, True, False, True, False, True]
print(a[mask])
# a[mask]=10
# print(a)


# 索引掩码
p = np.array(['Mi', 'Apple', 'Huawei', 'Oppo', 'Vivo'])
prices = [0, 4, 3, 2, 1]
print(p[prices])

# 输出1~100以内3的倍数
a = np.arange(1, 100)
print(a[a % 3 == 0])
print(a[(a % 3 == 0) & (a % 7 == 0)])

