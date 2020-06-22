"""
模型层
"""


class CommodityModel:
    """
        商品模型
    """

    def __init__(self, cid=0, name="", price=0.0):
        self.cid = cid
        self.name = name
        self.price = price
