"""
(选做) 2048 核心算法
(1). 创建全局变量二维列表作为2048地图
(2). 创建函数,向左移动
(3). 创建函数，向右移动
@author hailin
@date 2020-05-18
"""
list_merge = [2, 0, 2, 0]


# 定义零元素后移
def zero_to_end():
    """
    零元素向后移动
    从后向前遍历，如果是0则删除，在末尾追加0
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 合并函数
def merge():
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] *= 2
            del list_merge[i + 1]
            list_merge.append(0)


# (1). 创建全局变量二维列表作为2048地图:
map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]


# (2). 创建函数,向左移动
def move_to_left():
    """
    向左移动
    获取到map的每行line交给list_merge,再调用merge()进行合并
    """
    global list_merge
    for line in map:
        list_merge = line
        merge()


# (3). 创建函数，向右移动
def move_to_right():
    """
    向右移动
    获取到map的每行line切片反转后交给list_merge,再调用merge()进行合并，再交回给line[::-1]
    """
    global list_merge
    for line in map:
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge


# 定义显示方阵map
def show_map():
    for line in map:
        print(line)


show_map()
print("向左移动")
move_to_left()
show_map()
