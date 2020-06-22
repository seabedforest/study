"""
控制层，逻辑控制与计算
"""
class CommodityController:
    """
        商品逻辑控制:负责处理核心业务逻辑
    """

    def __init__(self):
        self.__list_commoditys = []  # type:List[CommodityModel]
        self.__start_id = 1001

    @property
    def list_commoditys(self):
        return self.__list_commoditys

    def add_commodity(self, commodity):
        commodity.cid = self.__start_id
        self.__start_id += 1
        self.__list_commoditys.append(commodity)

    def remove_commodity(self, cid):
        for i in range(len(self.list_commoditys)):
            if self.list_commoditys[i].cid == cid:
                del self.list_commoditys[i]
                return True
        return False