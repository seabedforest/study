"""
练习:使用装饰器，为旧功能增加新功能.
"""


# 新功能
def print_func(func):
    def wrapper(*args, **kwargs):
        print("执行了", func.__name__, "函数")
        return func(*args, **kwargs)
    return wrapper
# 旧功能
@print_func
def insert(data):
    print("插入", data, "成功")

@print_func
def delete(id):
    print("删除", id, "成功")


insert("ok")
delete(1001)
