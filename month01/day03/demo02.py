"""
    bool 运算
        整形int:  .... -2 -1 0 1 2 3 ...
            数学运算
        布尔bool:  成立(对)True    不成成立(错)False
            命题:带有判断性的陈述句
                我是一个总统
        转换为布尔:bool(数据)
        比较运算符:相同==   不同!=    >    <    >=    <=
    练习:exercise01

"""
# 命题:我是一个总统
result = input("请输入您的职位:") == "总统"
print(result)  # True False
# 转换为布尔:bool(数据)
# 结果为False: 零0    零点零0.0    空字符串""   空类型None
print(bool(None))
