"""
    运算符
        算数运算符: +    -    *    幂运算**  除法运算: /  //  %
        增强运算符:+=  -=    *=      **=           /=  //=  %=
                累加  累减
    练习:exercise06~10
"""
# 1. 算数运算符
# 3 的 4 次方
print(3 ** 4)  # 3 * 3 * 3 * 3
# 取小数商
print(5 / 2)  # 2.5
# 取整数商
print(5 // 2)  # 2
# 取余数
print(5 % 2)  # 1

# 2. 增强运算符:运算过后又给自身赋值
number = 5
number + 2 # 不影响number
print(number)  # 5

number = 5
# number = number + 2  # 运算过后又给自身赋值
number += 2  # 运算过后又给自身赋值
print(number)  # 7
