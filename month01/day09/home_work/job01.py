def func01(*args, **kwargs):
    print(args)
    print(kwargs)


def func02(p1, p2, *args, p3, p4=4):
    print(p1)
    print(p2)
    print(args)
    print(p3)
    print(p4)


func01([1, 2, 3, 4,6,7,8,0], {"a": 44, "b": 5})
func02(1,2,3,4,5,6,7,p3=10,p4=9)