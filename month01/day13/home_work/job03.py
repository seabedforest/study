"""
使用面向对象思想,描述下列情景.
    玩家攻击敌人(掉装备)
    敌人攻击玩家(碎屏)
    考虑:玩家和敌人还可能被其他目标攻击,也可能攻击其他目标.
    要求:增加新攻击目标,攻击方代码不变.
@author hailin
@date 2020-05-18
"""


class Scene:
    def attack(self, target):
        print("看拳")
        target.damage()

    def damage(self):
        pass


class Player(Scene):
    def damage(self):
        print("碎屏")


class Monster(Scene):
    def damage(self):
        print("掉装备")


class Boos(Scene):
    def damage(self):
        print("满地都是装备和材料")



xiaoming = Player()
gebulin = Monster()
guyanlong = Boos()
xiaoming.attack(gebulin)
xiaoming.attack(guyanlong)
gebulin.attack(xiaoming)

