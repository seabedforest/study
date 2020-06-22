"""
一张纸的厚度是0.01毫米
请计算，对折多少次超过珠穆朗玛峰(8844.43米). 30 次
"""
metters = 0.00001
count = 0
while metters <= 8844.43:
    metters *= 2
    count += 1
print(count)
# print(metters)

"""
一张纸的厚度是0.01毫米
请计算，对折36次的高度是多少米.
"""
metters = 0.00001
count = 1
while count <= 36:
    metters *= 2
    count += 1
print(metters)
