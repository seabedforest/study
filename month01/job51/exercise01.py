"""
给一个不多于 5 位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
@author hailin
@date 2020-05-03
"""
# 获取数字
number = input("请输入一个不多于5位的正整数：")
# 判断是几位数
l = len(number)
while True:
    if l > 5 or int(number) <= 0:
        number = input("这是个大于五位数的数字或负整数或零，请重新输入:")
        l = len(number)
    else:
        print("这是", l, "位数")
        # 逆序打印出各位数字
        for i in number[::-1]:
            print(i, end="")
        break
