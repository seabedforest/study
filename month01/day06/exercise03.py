"""
使用列表推导式生成1--50之间能被3或者5整除的数字
使用列表推导式生成5 -- 100之间的数字平方
"""
# 使用列表推导式生成1--50之间能被3或者5整除的数字
result01 = [num for num in range(1, 51) if num % 3 == 0 or num % 5 == 0]
print(result01)

result02 = [num ** 2 for num in range(5, 101)]
print(result02)
