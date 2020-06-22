"""
函数参数
实际参数
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


func01(1, 2, 3)
func01(p1=1, p2=2, p3=3)
func01(p2=2, p1=1, p3=3)


def func02(p1="", p2=0.0, p3=0):
    print(p1)
    print(p2)
    print(p3)


func02(p2=2)
func02(1, 2, 3)
