"""
4. 使用面向对象思想,描述下列情景.
    -- (1)小明使用手机打电话
    -- (2)小明一次请多个保洁打扫卫生
          效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.
          区别:保洁与保洁列表
@author hailin
@date 2020-05-16
"""


class Client:
    def __init__(self, name=""):
        self.name = name

    def useing(self):
        print(self.name + "使用手机打电话")

    def notify(self, household_service):
        self.useing()
        print("通知")
        household_service.cleaning()


class Cleaner:
    def __init__(self, *args):
        self.names = args

    def cleaning(self):
        floor = 0
        for name in self.names:
            floor += 1
            print(name + f"去{floor}楼打扫卫生")


xm = Client("小明")
cleaner_list = ["小华", "小花", "小李", "小刘", "小翠"]
cleaner = Cleaner(*cleaner_list)
xm.notify(cleaner)

