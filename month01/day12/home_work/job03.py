"""
-- (3)玩家攻击(攻击力)多个敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
      区别:敌人与敌人列表
@author hailin
@date 2020-05-16
"""


class Player:
    def __init__(self, hp=200, atk=50):
        self.atk = atk
        self.hp = hp

    def attack(self, target):
        print("玩家攻击")
        target.damage(self.atk)

    def damage(self, value):
        print("(⊙o⊙)… 玩家受伤啦")
        print("碎屏")
        self.hp -= value
        if self.hp <= 0:
            print("游戏结束")


class Enemy:
    def __init__(self, *args, hp=100, atk=10):
        self.names = args
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        count = len(self.names)
        for name in self.names:
            print(f"{name} 敌人受伤啦")
        self.hp -= value
        if self.hp <= 0:
            print("播放死亡动画")
            print(f"{count}连杀")

    def attack(self, target):
        print("敌人攻击")
        target.damage(self.atk)


enemy_list = ["1号敌人", "2号敌人", "3号敌人", "4号敌人", "5号敌人"]

p01 = Player()
e01 = Enemy(*enemy_list)
p01.attack(e01)
e01.attack(p01)
p01.attack(e01)
