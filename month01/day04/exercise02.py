"""
在终端中录入一个整数, 打印每位相加和。
"""
number = input("输入个整数:")
totle=0
for sum_number in number:
    totle += int(sum_number)
print("每位相加和为:"+str(totle))