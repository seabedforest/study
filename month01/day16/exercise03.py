"""
创建敌人类,敌人的攻击力在0-100之间.
在终端中获取攻击力,创建敌人对象.如果超过范围,重新输入.直到数据在有效范围内.
"""


class Enemy:
    def __init__(self, atk=0):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise Exception("攻击力超过范围", "0 <= 攻击力 <= 100")


while True:
    try:
        atk = int(input("请输入敌人的攻击力:"))
        en01 = Enemy(atk)
        print(en01.atk)
        break
    except Exception as e:
        print(e.args)
