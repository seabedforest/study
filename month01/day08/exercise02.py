"""
list01 = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
for line in list01:
for item in line:
print(item,end = "\t")
print()
"""
def print_list_elements(list_name):
    """
    打印二维列表中的各个元素
    :param list_name: 列表名称
    :return:
    """
    for line in list_name:
        for item in line:
            print(item, end="\t")
        print()

list01 = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
print_list_elements(list01)