"""
玩家攻击(攻击力)敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
敌人攻击(攻击力)玩家，玩家受伤(减血,碎屏)后可能si亡(游戏结束)
"""


class Personage:
    def __init__(self, name=""):
        self.name = name

    def attack(self, result):
        print(self.name, "攻击", result.die())


class Result:
    def die(self):
        print("播放si亡动画")


player = Personage("小明")
x = Result()
player.attack().attack(x)
