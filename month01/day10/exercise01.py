"""
创建狗类
数据：品种、爱称、年龄、体重
行为：吃、叫
实例化两个对象并调用其方法
画出内存图
"""


class Dogs:
    def __init__(self, breed, pet_name, age, weight):
        self.breed = breed
        self.pet_name = pet_name
        self.age = age
        self.weight = weight

    def eat(self):
        print(self.pet_name + "来吃午餐了")

    def cry(self):
        print(self.breed + "的叫声是'汪汪汪'")


z = Dogs("中华田园犬", "旺财", 1.5, 20)
t = Dogs("泰迪", "小迪", 1, 10)
z.eat()
t.cry()
