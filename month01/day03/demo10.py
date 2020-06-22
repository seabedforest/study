"""
    while 循环
        死循环
            while True:
                循环体
                if 退出条件:
                    break
    练习:exercise12

"""
while True:
    sex = input("请输入性别：")
    if sex == "男":
        print("您好，先生！")
    elif sex == "女":
        print("您好，女士！")
    else:
        print("性别未知")
    if input("如果继续,请输入e:") != "e":
        break  # 退出循环
