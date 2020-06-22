"""
5. list01 = [6,2,3,4,5,6,7,3,2,4,8]
    定义函数,删除列表中重复元素.(不使用其他容器,自定义算法)
@author hailin
@date 2020-05-17
"""


def delete_duplicate_elements_of_list(list_target):
    for element in list_target:
        if list_target.count(element) > 1:
            list_target.remove(element)
            delete_duplicate_elements_of_list(list_target)


list01 = [6, 2, 3, 4, 5, 6, 7, 3, 2, 4, 8, 8, 8]
delete_duplicate_elements_of_list(list01)
print(list01)


def func2(one_list):
    '''
    使用字典的方式
    '''
    return {}.fromkeys(one_list).keys()


one_list = [56, 7, 4, 23, 56, 9, 0, 56, 12, 3, 56, 34, 45, 5, 6, 56]
func2(one_list)
print(func2(one_list))