"""
打印出3/9/12
(每行一个)循环打印6, 7, 8, 9, 10
(每行一个)循环打印15,14,13,12,11
(每行一个)循环打印1,6,11
(每行一个)循环打印14,9,4
以表格状打印每个元素(不要逗号)
"""

list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
# 打印出3/9/12
print(list01[0][2], list01[1][3], list01[2][1])

# (每行一个)循环打印6, 7, 8, 9, 10
for num in range(len(list01[0])):
    print(list01[1][num])

# (每行一个)循环打印15,14,13,12,11
for num in range(len(list01[0]) - 1, -1, -1):
    print(list01[-1][num])

# (每行一个)循环打印1,6,11
for num in range(len(list01)):
    print(list01[num][0])
# (每行一个)循环打印14,9,4
for num in range(len(list01) - 1, -1, -1):
    print(list01[num][3])

# 以表格状打印每个元素(不要逗号)
# for i in range(len(list01)):
#     for j in range(len(list01[0])):
#         print(list01[i][j],end=" ")
#     print()

for i in list01:
    for j in i:
        print(j, end="\t")
    print()
