# 需求: 保护数据,在有效范围内.
# 保障老婆的年龄在22到100之间

class Wife:
    def __init__(self, name="", age=0):
        # 快捷键: alt + 回车 --> 自动生成代码
        self.name = name
        self.age = age  # 调用def age(self, value)方法 age(25)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 22 <= value <= 100:
            self.__age = value
        else:
            raise Exception("超过结婚年龄")  # 产生错误


w01 = Wife("双儿", 25)
print(w01.age)  # 调用def age(self)方法
