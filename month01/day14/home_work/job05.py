"""
参照info_manager_system.py的框架结构
   完成商品信息管理系统
@author hailin
@date 2020-05-20
"""
from typing import List


class CommodityModel:
    """
        商品信息模型
    """

    def __init__(self, cid=0, name='', price=0.0):
        """
        商品各种数据
        :param cid: 商品编号
        :param name: 商品名称
        :param price: 商品单价
        """
        self.cid = cid
        self.name = name
        self.price = price


class CommodityView:
    """
    商品信息显示界面：负责处理界面逻辑(输入/输出/界面跳转)
    """

    def __init__(self):
        self.__controller = CommodityController()

    def __display_menu(self):
        print("1) 添加商品信息")
        print("2) 显示所有的商品信息")
        print("3) 删除商品信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()


    def __input_commodity(self):
        commodity = CommodityModel()  # type:CommodityModel
        commodity.name = input("请输入商品名称:")
        commodity.price = float(input("请输入商品的单价:"))
        self.__controller.add_commodity(commodity)

    def __display_commoditys(self):
        for commodity in self.__controller.commodity_list:
            print(f"{commodity.name}的商品编号是{commodity.cid},单价是{commodity.price}")

    def __delete_commodity(self):
        cid = int(input("请输入要删除的商品编号:"))
        if self.__controller.remove_commodity(cid):
            print(f"商品编号为{cid},已删除")
        else:
            print("删除失败")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()


class CommodityController:
    """
        商品逻辑控制:负责处理核心业务逻辑
    """

    def __init__(self):
        self.__commodity_list = []  # type:List[CommodityModel]
        self.__start_id = 1001

    @property
    def commodity_list(self):
        return self.__commodity_list

    def add_commodity(self, commodity):
        commodity.cid = self.__start_id
        self.__start_id += 1
        self.__commodity_list.append(commodity)

    def remove_commodity(self, cid):
        for i in range(len(self.__commodity_list)):
            if self.__commodity_list[i].cid == cid:
                del self.__commodity_list[i]
                return True
        return False


# 入口
view = CommodityView()
view.main()
