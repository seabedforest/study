"""
5.创建技能类(技能名称,攻击比率,消耗法力,持续时间)
  保证数据范         0 - 2  0 - 80  0 - 120
@author hailin
@date 2020-05-15
"""


class Skills:
    def __init__(self, name, rate, mp, time):
        self.skill_name = name
        self.attack_rate = rate
        self.mana_cost = mp
        self.duration = time

    @property
    def attack_rate(self):
        return self.__attack_rate

    @attack_rate.setter
    def attack_rate(self, valuse):
        if 0 <= valuse <= 2:
            self.__attack_rate = valuse
        else:
            raise Exception("超过攻击力范围")

    @property
    def mana_cost(self):
        return self.__mana_cost

    @mana_cost.setter
    def mana_cost(self, valuse):
        if 0 <= valuse <= 80:
            self.__mana_cost = valuse
        else:
            raise Exception("超过消耗法力范围")

    @property
    def duration(self):
        return self.__mana_cost

    @duration.setter
    def duration(self, valuse):
        if 0 <= valuse <= 120:
            self.__duration = valuse
        else:
            raise Exception("超过持续时间范围")


wo = Skills("火爆甜心", 2, 79, 120)
