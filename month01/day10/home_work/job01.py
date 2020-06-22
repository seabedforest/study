"""
3. 洞察你身边的客观事物,挑选2个创建类和对象.
    目标:使用计算机描述生活
    体会:现实事物  -抽象->  类  -具体-> 对象
"""
class IntelligentDevice :
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def use(self):
        print("使用%s上网冲浪" % self.name)


callphone = IntelligentDevice("华为手机",2000)
callphone.use()
computer = IntelligentDevice("战神笔记本",5100)
computer.use()


class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))
        print(self.__weight)


# 实例化类
p = people('runoob', 10, 30)
p.speak()

