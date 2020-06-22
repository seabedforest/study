"""
创建父类：车(品牌，速度)
创建子类：电动车(电池容量,充电功率)
创建子类对象并画出内存图。
"""


class Vehicle:
    def __init__(self, brand="", speed=0):
        self.brand = brand
        self.speed = speed


class Electrocar(Vehicle):
    def __init__(self, brand, speed, battery_capacity, charging_power):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power


che01 = Electrocar("海马电瓶车", 100, 20000, 2000)
print(che01.__dict__)
print(che01.brand)
print(che01.speed)
print(che01.battery_capacity)
print(che01.charging_power)
