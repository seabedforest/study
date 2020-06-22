"""
5. 将列表中整数的个位不是5和3的数字存入另外一个列表
    list03 = [25, 63, 27, 75, 70, 83, 27]
    结果:[27, 70, 27]
@author hailin
@date 2020-05-07
"""
# 列表数据
list03 = [25, 63, 27, 75, 70, 83, 27]
list04 = []
# 运算过程，获取到新列表list04
for num in list03:
    if num % 10 != 5 and num % 10 != 3:
        list04.append(num)
# 显示结果
print(list04)
