"""
函数参数
实际参数
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


list01 = [[1], [2], [3]]
func01(*list01)
dict02 = {"p1": 1, "p2": 2, "p3": 3}
func01(**dict02)


def func03(*args):
    print(args)


func03(1, 2, 3)
func03()
# func03(a=1, b=2)
