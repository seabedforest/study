"""
2000至3200之间（均包括在内）,找到所有可以被7整除但不是5的倍数的数字。获得的数字应以逗号分隔的顺序打印在一行上。
@author hailin
@date  2020-05-03
"""
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=",")
