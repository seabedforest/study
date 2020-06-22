"""
累加0 1 2 3 4 5 6 7 8
累加3 4 5 6 7 8 9 10
累加2 4 6 8 10 12
累加8 7 6 5 4 3
累加-1 -2 -3 -4 -5 -6
"""
# 累加0 1 2 3 4 5 6 7 8
sums = 0
for num in range(9):
    sums += num
print("和为:" + str(sums))

#累加3 4 5 6 7 8 9 10
sums = 0
for num in range(3,11):
    sums += num
print("和为:" + str(sums))

#累加2 4 6 8 10 12
sums = 0
for num in range(2,13,2):
    sums += num
print("和为:" + str(sums))

#累加8 7 6 5 4 3
sums = 0
for num in range(8,2,-1):
    sums += num
print("和为:" + str(sums))

#累加-1 -2 -3 -4 -5 -6
sums = 0
for num in range(-7,-1):
    sums += num
print("和为:" + str(sums))