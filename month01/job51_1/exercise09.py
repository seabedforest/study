"""
while 循环累加练习
使用while循环累加下列数字：0 + 1 + 2 + 3
使用while循环累加下列数字：2 + 3 + 4 + 5 + 6
使用while循环累加下列数字：1 + 3 + 5 + 7
使用while循环累加下列数字：8 + 7 + 6 + 5 + 4
使用while循环累加下列数字：-1+  -2 + -3 + -4 + -5
"""
# 使用while循环累加下列数字：0 + 1 + 2 + 3
number = 0
total = 0
while number <= 3:
    total += number
    number += 1
print("0 + 1 + 2 + 3为:", total)

# 使用while循环累加下列数字：2 + 3 + 4 + 5 + 6
number = 2
total = 0
while number <= 6:
    total += number
    number += 1
print("2 + 3 + 4 + 5 + 6为:", total)

# 使用while循环累加下列数字：1 + 3 + 5 + 7
number = 1
total = 0
while number <= 7:
    total += number
    number += 2
print("1 + 3 + 5 + 7为:", total)

# 使用while循环累加下列数字：8 + 7 + 6 + 5 + 4
number = 8
total = 0
while number >= 4:
    total += number
    number -= 1
print("8 + 7 + 6 + 5 + 4为:", total)

# 使用while循环累加下列数字：-1+  -2 + -3 + -4 + -5
number = -1
total = 0
while number >= -5:
    total += number
    number -= 1
print("-1+  -2 + -3 + -4 + -5为:", total)
