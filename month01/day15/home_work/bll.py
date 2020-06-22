"""
    业务business 逻辑logic 层layer
@author hailin
@date 2020-05-21
"""
from models import Game2048Model


class Game2048Controller:
    def __init__(self):
        self.map = [
            [2, 0, 0, 2],
            [4, 2, 0, 2],
            [2, 4, 2, 4],
            [0, 4, 0, 4],
        ]
        self.__matrix_map = Game2048Model()

    # 定义零元素后移
    def __zero_to_end(self):
        """
        零元素向后移动
        从后向前遍历，如果是0则删除，在末尾追加0
        """
        for i in range(len(self.__matrix_map.list_merge) - 1, -1, -1):
            if self.__matrix_map.list_merge[i] == 0:
                del self.__matrix_map.list_merge[i]
                self.__matrix_map.list_merge.append(0)

    # 合并函数
    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__matrix_map.list_merge) - 1):
            if self.__matrix_map.list_merge[i] == self.__matrix_map.list_merge[i + 1]:
                self.__matrix_map.list_merge[i] *= 2
                del self.__matrix_map.list_merge[i + 1]
                self.__matrix_map.list_merge.append(0)

    # 定义向左移动
    def move_to_left(self):
        """
        向左移动
        获取到map的每行line交给list_merge,再调用merge()进行合并
        """
        for line in self.map:
            self.__matrix_map.list_merge = line
            self.__merge()

    # 定义向右移动
    def move_to_right(self):
        """
        向右移动
        获取到map的每行line切片反转后交给list_merge,再调用merge()进行合并，再交回给line[::-1]
        """
        for line in self.map:
            self.__matrix_map.list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__matrix_map.list_merge

    # 方阵转置
    def __square_matrix_transpose(self, matrix_list):
        """
        方阵转置,列转为行
        :param matrix_list: 需转置的方阵
        :return:
        """
        for r in range(1, len(matrix_list)):
            for c in range(r, len(matrix_list)):
                matrix_list[c][r - 1], matrix_list[r - 1][c] = matrix_list[r - 1][c], matrix_list[c][r - 1]

    # 定义向上移动
    def move_to_up(self):
        """
        向上移动
        先进行方阵转置，再进行向左移动，最后方阵转置回去
        """
        self.__square_matrix_transpose(self.map)
        self.move_to_left()
        self.__square_matrix_transpose(self.map)

    # 定义向下移动
    def move_to_down(self):
        """
        向下移动
        先进行方阵转置，再进行向右移动，最后方阵转置回去
        """
        self.__square_matrix_transpose(self.map)
        self.move_to_right()
        self.__square_matrix_transpose(self.map)
