"""
创建敌人类
创建实例变量并保证数据在有效范围内
姓名、血量、攻击力、防御力
0-100 1 – 30、 0 – 20
"""


class Enemy:
    def __init__(self, name='', hp=0, atk=1, ac=0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.ac = ac

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise Exception("超过血量范围")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 1 <= value <= 30:
            self.__atk = value
        else:
            raise Exception("超过攻击力范围")

    @property
    def ac(self):
        return self.__ac

    @ac.setter
    def ac(self, value):
        if 0 <= value <= 20:
            self.__ac = value
        else:
            raise Exception("超过防御力范围")


diren01 = Enemy("qtx", 20, 5, 0)
print(diren01.name)
print(diren01.atk)
print(diren01.ac)
print(diren01.hp)
