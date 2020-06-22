"""
通过属性限制数据范围,体会属性的继承
父类：车(品牌，速度)
             0-280
创建子类：电动车(电池容量,充电功率)
              0 - 50000  200 - 250
@author hailin
@date 2020-05-16
"""


class Vehicle:
    """
    车类
    """

    def __init__(self, brand="", speed=0):
        """
        车(品牌，速度)
        :param brand: 品牌
        :param speed: 速度
        """
        self.brand = brand
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            self.__speed = 0
        elif value > 280:
            self.__speed = 280
        else:
            self.__speed = value


class Electrocar(Vehicle):
    """
    电动车
    """

    def __init__(self, brand="", speed=0, battery_capacity=0, charging_power=200):
        """
        电动车各种属性数据
        :param battery_capacity: 电池容量
        :param charging_power: 充电功率
        """
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value):
        if value < 0:
            self.__battery_capacity = 0
        elif value > 50000:
            self.__battery_capacity = 50000
        else:
            self.__battery_capacity = value

    @property
    def charging_power(self):
        return self.__charging_power

    @charging_power.setter
    def charging_power(self, value):
        if value < 200:
            self.__charging_power = 200
        elif value > 250:
            self.__charging_power = 250
        else:
            self.__charging_power = value


electromobile01 = Electrocar("爱狮", 281, 50001, 400)
print(electromobile01.__dict__)