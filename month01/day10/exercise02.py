"""
创建手机类
数据：品牌、价格、颜色
行为：通话
实例化两个对象并调用其方法
"""

class MobilePhone:
    def __init__(self,brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print("%s能免费享受500分中长途通话" % self.brand)


huawei = MobilePhone("huawei",5600,"red")
huawei.call()
iphone = MobilePhone("iphone",7600,"blue")
iphone.call()

def func01(p1):
    p1.color = "红色"

func01(huawei)
print(huawei.color)


list01 = [
MobilePhone("huawei",5600,"red"),MobilePhone("iphone",7600,"blue")
]

print(list01)