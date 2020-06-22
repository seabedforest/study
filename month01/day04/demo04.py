"""
    continue 跳过
    练习:exercise04
"""
# 累加1--100之间数字
# 条件:能被3整除的数字
# sum_value = 0
# for number in range(1, 101):
#     # 满足条件 干
#     if number % 3 == 0:
#         sum_value += number
# print(sum_value)

sum_value = 0
for number in range(1, 101):
    # 不满足条件 跳过
    if number % 3 != 0:
        continue
    sum_value += number
print(sum_value)
