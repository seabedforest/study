# 4. 输出打印结果
def func03(*args, **kwargs):
    print(args)
    print(kwargs)


list01 = [1, 2, 3, 4, 5]
dict02 = {"a": 1, "b": 2, "c": 3}
func03(*list01, **dict02)
