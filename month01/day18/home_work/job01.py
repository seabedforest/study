"""
    外部嵌套作用域
"""


# 外函数
def func01():
    # 局部变量：相对于全局而言
    # 外部嵌套变量：相对于内函数而言
    a = 10

    # 内函数
    def func02():
        # 读取外部嵌套变量
        print(a)

    # 调用内函数
    func02()


# 调用外函数
func01()



def func03():
    a = 10

    def func04():
        # 内部函数修改外部嵌套变量
        nonlocal a
        a = 100

    func04()
    print(a)

func03()