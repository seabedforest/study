"""
7. (选做) 2048 核心算法
    1. 定义全局变量
        list_merge = [2,0,2,0]

    2. 定义函数,将list_merge的零元素移动到末尾　zero_to_end()
         [2,0,2,0]  -->  [2,2,0,0]
         [2,0,0,2]  -->  [2,2,0,0]
         [2,4,0,2]  -->  [2,4,2,0]

    3. 定义函数,将list_merge的相同元素合并 merge()
         [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
         [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
         [4,4,4,4]  -->  [8,8,0,0]
         [2,0,4,2]  -->  [2,4,2,0]
         [2,2,4,8]
@author hailin
@date 2020-05-17
"""
# 1.定义全局变量
list_merge01 = [2, 0, 2, 0]
list_merge02 = [2, 0, 0, 2]
list_merge03 = [2, 4, 0, 2]


# 2. 定义函数,将list_merge的零元素移动到末尾　zero_to_end()
def zero_to_end(list_merge):
    for _ in range(3):
        for i in range(3):
            if 0 == list_merge[i]:
                list_merge[i] = list_merge[i + 1]
                list_merge[i + 1] = 0


zero_to_end(list_merge01)
zero_to_end(list_merge02)
zero_to_end(list_merge03)
print(list_merge01, list_merge02, list_merge03)


# 3. 定义函数,将list_merge的相同元素合并 merge()
def merge(list_merge):
    for i in range(3):
        zero_to_end(list_merge)
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] *= 2
            list_merge[i + 1] = 0


list_merge04 = [2, 0, 2, 0]
list_merge05 = [2, 0, 0, 2]
list_merge06 = [4, 4, 4, 4]
list_merge07 = [2, 0, 4, 2]
list_merge08 = [2, 2, 4, 8]
merge(list_merge04)
merge(list_merge05)
merge(list_merge06)
merge(list_merge07)
merge(list_merge08)
print(list_merge04, list_merge05, list_merge06, list_merge07, list_merge08)
