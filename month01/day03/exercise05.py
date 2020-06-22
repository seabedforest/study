"""
    练习:根据性别,打印信息
        您好，先生
        您好，女士
        性别未知
"""
sex = input("请输入性别：")
if sex == "男":
    print("您好，先生！")
elif sex == "女":
    print("您好，女士！")
else:
    print("性别未知")
