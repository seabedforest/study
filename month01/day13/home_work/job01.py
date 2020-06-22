"""
内置可重写函数练习1
(1). 创建父子类,添加实例变量
        创建父类:人(姓名,年龄)
        创建子类:学生(成绩)
(2). 创建父子对象,直接打印.
        格式: 我是xx,今年xx.
             我是xx,今年xx,成绩是xx.
(3). 通过eval + __repr__拷贝对象,体会修改拷贝前的对象名称,不影响拷贝后的对象.
@author hailin
@date 2020-05-18
"""


# (1). 创建父子类,添加实例变量
class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f"我是{self.name},今年{self.age}."

    def __repr__(self):
        return "Person('%s',%d)" % (self.name, self.age)


class Student(Person):
    def __init__(self, name="", age=0, score=0):
        super().__init__(name, age)
        self.score = score

    def __str__(self):
        # return f"我是{self.name},今年{self.age},成绩是{self.score}."
        return super().__str__() + f"成绩是{self.score}."

    def __repr__(self):
        return "Student('%s',%d,%d)" % (self.name, self.age, self.score)


# (2). 创建父子对象,直接打印.
hailin = Person("海林", 18)
xiaohua = Student("小华", 20, 96)
print(hailin)
print(xiaohua)

# (3). 通过eval + __repr__拷贝对象,体会修改拷贝前的对象名称,不影响拷贝后的对象.
str_code = hailin.__repr__()
xiaoming = eval(str_code)
hailin.name = "海底森林"
print(xiaoming.name)
