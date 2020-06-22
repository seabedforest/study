"""
在终端中获取一个整数，作为边长，打印矩形。
"""
length_of_side = int(input("请输入边长:"))

for i in range(1,length_of_side+1):
    if 1< i < length_of_side:
        print("*"+" "*(length_of_side-2)+"*")
    else:
        print("*"*length_of_side)