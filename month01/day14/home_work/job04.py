"""
(选做)2048完成向上/向下移动
@author hailin
@date 2020-05-20
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


# 绑定一个 4 x 4 列表,初始值如下:
map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]


# 定义向左移动
def move_to_left():
    """
    向左移动
    获取到map的每行line交给list_merge,再调用merge()进行合并
    """
    global list_merge
    for line in map:
        list_merge = line
        merge()


# 定义向右移动
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


# 方阵转置
def square_matrix_transpose(matrix_list):
    """
    方阵转置,列转为行
    :param matrix_list: 需转置的方阵
    :return:
    """
    for r in range(1, len(matrix_list)):
        for c in range(r, len(matrix_list)):
            matrix_list[c][r - 1], matrix_list[r - 1][c] = matrix_list[r - 1][c], matrix_list[c][r - 1]


# 定义向上移动
def move_to_up():
    """
    向上移动
    先进行方阵转置，再进行向左移动，最后方阵转置回去
    """
    square_matrix_transpose(map)
    move_to_left()
    square_matrix_transpose(map)


# 定义向下移动
def move_to_down():
    """
    向下移动
    先进行方阵转置，再进行向右移动，最后方阵转置回去
    """
    square_matrix_transpose(map)
    move_to_right()
    square_matrix_transpose(map)


# 定义显示方阵map
def show_map():
    for line in map:
        print(line)


show_map()
print("向上移动")
move_to_up()
show_map()
