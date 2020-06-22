"""
玩家(攻击力)攻击敌人(血量)(掉装备),还可能死亡(播放死亡动画)
敌人(攻击力)攻击玩家(血量)(碎屏),还可能死亡(游戏结束)
@author hailin
@date 2020-05-19
"""


class Character:
    def __init__(self, atk=10, hp=100):
        self.atk = atk
        self.hp = hp

    # 所有角色攻击方式相同
    def attack(self, target):
        print("看我天马流星拳")
        target.damage(self.atk)

    # 所有角色受伤逻辑不同
    def damage(self,value):
        pass


class Player(Character):
    def damage(self,value):
        super().damage(value)
        print("碎屏")
        self.hp -= value
        if self.hp <= 0:
            print("game over")


class Enemy(Character):
    def damage(self, value):
        super().damage(value)
        print("掉装备")
        self.hp -= value
        if self.hp <= 0:
            print("播放死亡动画")

p01 = Player(200)
e01 = Enemy()
p01.attack(e01)
e01.attack(p01)
