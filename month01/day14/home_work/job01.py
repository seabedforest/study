"""
小明使用手机打电话
    要求:增加座机,卫星电话时不影响小明.
    写出案例中体现的面向对象三大特征和六大原则.
        三大特征
            封装:根据需求创建通讯工具类,手机类,座机类,卫星电话类.
            继承:创建通讯工具类,统一手机类,座机类,卫星电话类,隔离人员类与具体通讯工具的变化.
            多态:人员类调用通讯工具类,手机类,座机类,卫星电话类重写拨打方法
                  人员类进行通讯工具的使用
        六大原则
            开闭原则:增加各种通讯工具,人员类不改变.
            单一职责:
                通讯工具类负责管理所有通讯工具
                手机类负责其拨打方法
                座机类负责其拨打方法
                卫星电话类负责其拨打方法
            依赖倒置:人员类调用通讯工具类,不调用具体通讯工具(手机类,座机类,卫星电话类)
            组合复用:人员类与通讯工具类的拨打方式是组合关系
            里氏替换:人类打电话函数的形参是通信工具,调用时传递各种具体通信工具.
            迪米特:人类 与 具体通信工具低耦合
                  各种通信工具之间低耦合

@author hailin
@date 2020-05-19
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def use(self, tools):
        print(self.name + tools.Call())


class Communication_tools:
    def __init__(self, brand=''):
        self.brand = brand  # type: str

    def Call(self):
        pass

class MobilePhone(Communication_tools):

    def __init__(self, brand=''):
        super().__init__(brand)

    def Call(self):
        return f"使用{self.brand}打电话"


class Special_plane(Communication_tools):

    def __init__(self, brand=''):
        super().__init__(brand)

    def Call(self):
        return f"使用{self.brand}打长途电话"

class Satellite_phone(Communication_tools):

    def __init__(self, brand=''):
        super().__init__(brand)

    def Call(self):
        return f"使用{self.brand}打加密电话"
xiaoming = Person("小明")
huawei = MobilePhone("华为2")
zhuanji =Special_plane("家庭座机")
jiami = Satellite_phone("卫星电话")
xiaoming.use(huawei)
xiaoming.use(zhuanji)
xiaoming.use(jiami)