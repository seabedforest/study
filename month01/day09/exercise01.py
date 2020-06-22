"""
根据下列代码,定义函数,对列表进行升序排列
list01 = [4 54 5 6 67 788]
for r in range(len(list01) - 1):
for c in range(r + 1 len(list01)):
if list01[r] > list01[c]:
list01[r] list01[c] = list01[c] list01[r]
print(list01)
"""


def get_ascending_sort(variable_sequence):
    for r in range(len(variable_sequence) - 1):
        for c in range(r+1, len(variable_sequence)):
            if variable_sequence[r] > variable_sequence[c]:
                variable_sequence[r], variable_sequence[c] = variable_sequence[c], variable_sequence[r]


list01 = [4, 54, 5, 6, 67, 788]
get_ascending_sort(list01)
print(list01)
