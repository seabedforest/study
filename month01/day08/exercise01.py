"""
定义函数, 在一行中打印一维列表各元素
"""


def print_list_elements(list_name):
    """
    在一行中打印一维列表各元素
    :param list_name:  列表名称
    :return:
    """
    for item in list_name:
        print(item, end=" ")
    print()


list01 = [2, 3, 4, 56]
list02 = ["a", "b", "c", "d"]

print_list_elements(list01)
print_list_elements(list02)
