"""
    变量
        问题一:程序运行在哪里?  --- 内存中
        问题二:程序在处理什么?  --- 数据
        作用:在内存中操作数据
        语法1:变量名 = 数据
        语法2:变量名1,变量名2 = 数据1,数据2
        语法3:变量名1= 变量名2 = 数据1

    练习:exercise03

"""
# name = input("请输入姓名:")
# print(name)  # 陈映州 / 于全胜 / 陈灿坚

# 写法1:
name01 = "陈映州"  # 创建变量关联数据
name01 = "王娜娜"  # 修改变量关联的数据
name02 = "于全胜"  # 创建变量关联数据
print("name01")  # 打印出固定文字
print(name01)  # 打印变量(可以变化的数据)   王娜娜
# 写法2:
name03, name04 = "何雪超", "柯良"
# 写法3:
# 数据赋值给变量,传递的是数据地址
# 变量赋值给变量,传递的是变量存储的数据地址
name05 = name06 = "党卫"