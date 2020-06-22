from bll import HouseManagerController


class HouseManager:
    def __init__(self):
        self.__controller = HouseManagerController()
        self.secede = True
    def __display_menu(self):
        print("1.txt) 显示所有房源信息")
        print("2) 显示最贵的房源信息")
        print("3) 显示最小面积的房源")
        print("4) 获取所有户型种类{ 户型 ： 数量 }")
        print("5) 退出")
    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1.txt":
            self.__display_house()
        elif item == "2":
            self.__show_max_price()
        elif item == "3":
            self.__show_min_area()
        elif item == "4":
            self.__show_house_type()
        elif item == "5":
            self.secede = False

    def __display_house(self):
        for house in self.__controller.list_houses:
            print(house.__dict__)

    def main(self):
        while self.secede:
            self.__display_menu()
            self.__select_menu()

    def __show_max_price(self):
        house = self.__controller.get_house_by_max_price()
        print(house.__dict__)

    def __show_min_area(self):
        house = self.__controller.get_house_by_min_area()
        print(house.__dict__)

    def __show_house_type(self):
        dict_house_type = self.__controller.get_house_type()
        for k,v in dict_house_type.items():
            print("户型是%s,数量是%d" % (k,v))