"""
4. 将列表中的数字累乘5 * 1 * 4 ....
    list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
    结果：806400
@author hailin
@date 2020-05-07
"""
# 列表数据
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
# 计算过程
sum_totle = 1
for num in range(len(list02)):
    sum_totle *= list02[num]
# 显示结果
print(f"列表中的数字累乘5 * 1 * 4 ....结果为:{sum_totle}")
