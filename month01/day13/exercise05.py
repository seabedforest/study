"""
手雷爆炸,伤害了玩家(碎屏)和敌人(掉装备)
要求:当增加其他事物,不影响手雷的代码.
可能:鸭子(上天)....
体会:开闭原则
依赖倒置
继承价值
"""


class Grenade:
    def blast(self, target):
        print("手雷爆炸啦")
        target.damage()

class Explosion_object:
    def damage(self):
        pass


class Player(Explosion_object):
    def damage(self):
        print("碎屏")


class Enemy(Explosion_object):
    def damage(self):
        print("掉装备")

grenade = Grenade()
grenade.blast(Player())
grenade.blast(Enemy())