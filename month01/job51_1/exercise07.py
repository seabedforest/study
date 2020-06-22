"""
梯形面积： （上底 + 下底) * 高  / 2
    在终端中获取上底/下底/高
    打印面积
@author hailin
@date 2020-05-03
"""
# 获取梯形的上底、下底和高
upper_base = float(input("请输入梯形的上底:"))
bottom = float(input("请输入梯形的下底:"))
height = float(input("请输入梯形的高:"))
# 公式求面积
area = (upper_base + bottom) * height / 2
# 显示结果
print("梯形的面积为:", area)
