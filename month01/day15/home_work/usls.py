"""
    用户user 显示show 层layer
@author hailin
@date 2020-05-21
"""
from bll import Game2048Controller
from models import Game2048Model


class Game2048View:
    """
    2048游戏界面视图，负责处理界面逻辑
    """

    def __init__(self):
        self.__controller = Game2048Controller()
        self.__matrix_map = Game2048Model()

    def show_map(self):
        for line in self.__controller.map:
            print(line)

    def select_menu(self):
        option = input("输入移动方式'w、s、a、d键来用上下左右移动':")
        if option == "a":
            self.__controller.move_to_left()
        if option == "d":
            self.__controller.move_to_right()
        if option == "w":
            self.__controller.move_to_up()
        if option == "s":
            self.__controller.move_to_down()
