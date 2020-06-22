"""
创建子类：狗(跑)，鸟类(飞)
创建父类：动物(吃)
体会子类复用父类方法
"""


class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def running(self):
        print("跑")
        super().eat()

class Brid(Animal):
    def flying(self):
        print("飞")
        super().eat()

d = Dog()
d.running()
b = Brid()
b.flying()
