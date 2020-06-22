"""
-- (4)
    张无忌教赵敏九阳神功
    赵敏教张无忌玉女心经
    张无忌工作挣了5000元
    赵敏工作挣了10000元
@author hailin
@date 2020-05-16
"""


class Person:
    def __init__(self, name):
        self.name = name

    def teach(self, name, kungfu):
        print("%s教%s%s" % (self.name, name, kungfu))

    def work(self, money):
        print("%s作挣了%.2f元" % (self.name, money))


zwj = Person("张无忌")
zwj.teach("赵敏", "九阳神功")

zm = Person("赵敏")
zm.teach("张无忌", "玉女心经")

zwj.work(5000)
zm.work(10000)