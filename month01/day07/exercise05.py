"""
list01 = [4, 54, 5, 6, 67, 788]
进行升序排列(小 --> 大)
"""
list01 = [4, 54, 5, 6, 67, 788]

for r in range(len(list01)-1):
    for c in range(r+1,len(list01)):
        if list01[r] > list01[c]:
            list01[r],list01[c] = list01[c],list01[r]
print(list01)