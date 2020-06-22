"""
视图层
"""
from bll01 import CommodityController
from model01 import CommodityModel


class CommodityView:
    """
        商品视图:负责处理界面逻辑(输入/输出/界面跳转)
    """

    def __init__(self):
        self.__controller = CommodityController()
        self.secede = True

    def __display_menu(self):
        print("1) 添加商品信息")
        print("2) 显示所有商品信息")
        print("3) 删除商品信息")
        print("4) 退出")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.secede = False

    def __input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称:")
        commodity.price = self.get_int("商品单价:")

        self.__controller.add_commodity(commodity)

    def get_int(self, commodity):
        while True:
            try:
                data = int(input(f"请输入{commodity}"))
                return data
            except:
                print(f"输入的{commodity}错误")

    def main(self):
        while self.secede:
            self.__display_menu()
            self.__select_menu()

    def __display_commoditys(self):
        for commodity in self.__controller.list_commoditys:
            print(f"{commodity.name}的编号是{commodity.cid},单价是{commodity.price}")

    def __delete_commodity(self):
        cid = self.get_int("商品编号:")
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")
