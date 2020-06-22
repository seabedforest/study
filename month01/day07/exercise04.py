"""
# 在下列元组中,查找最小值
tuple01 = (43,54,5,6,76,8,9)
"""
tuple01 = (43,54,5,6,76,8,9)
min_value = tuple01[0]
for i in  range(1,len(tuple01)):
    if min_value > tuple01[i]:
        min_value = tuple01[i]
print(min_value)