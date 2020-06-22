"""
参照info_manager_system.py的框架结构
   完成商品信息管理系统

@author hailin
@date 2020-05-19
"""
from typing import List


class CommodityModel:
    """
        商品信息模型
    """

    def __init__(self, cid=0, name="", price=0):
        self.cid = cid  # 对商品信息的唯一标识
        self.name = name
        self.price = price


class CommodityView:
    """
        商品信息视图:负责处理界面逻辑(输入/输出/界面跳转)
    """

    def __init__(self):
        self.controller = CommodityController()

    def display_menu(self):
        print("1) 添加商品信息")
        print("2) 显示所有商品信息")
        print("3) 删除商品信息")

    def select_menu(self):
        item = input("请输入选项")
        if item == "1":
            self.input_commodity()
        elif item == "2":
            self.controller.show_commdity()
        elif item == "3":
            pass

    def input_commodity(self):
        commodity = CommodityModel()  # type CommodityModel
        commodity.name = input("请输入商品名称")
        commodity.price = float(input("请输入商品售价"))


class CommodityController:
    """
        商品信息逻辑控制，负责处理核心业务逻辑
    """

    def __init__(self):
        self.list_commoditys = []  # type:List[CommodityModel]
        self.start_cid = 1001

    def add_commdity(self, commodity):
        commodity.cid = self.start_cid
        self.start_cid += 1  # 商品编号自增长
        self.list_commoditys.append(commodity)

    def show_commdity(self):
        for item in self.list_commoditys:
            print(item.__dict__)

# 入口
view = CommodityView()
view.display_menu()
view.select_menu()
view.select_menu()