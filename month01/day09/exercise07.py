def func01(*, a, b, c):
    print(a)
    print(b)
    print(c)


func01(a=1, b=3, c=5)


def func02(g, *, a, b, c):
    print(a)
    print(b)
    print(c)
    print(g)

func02(10, a=1, b=3, c=5)

def func06(**kwargs):
    print(kwargs)

func06()
func06(a=1,b=2)
#func06(1234)