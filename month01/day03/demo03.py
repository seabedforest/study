"""
    逻辑运算符
        判断多个命题关系
        与 and   并且  -->  都满足
        或 or    或者  -->  一个就行
        非 not   反过来
    练习:exercise02/03

"""
# 丈母娘:
# 有钱吗?    有车吗?    有房吗?

# 　命题：有房　又  有车
# input("你有房子吗?") == "有"
# input("你有车子吗?") == "有"
# print(input("你有房子吗?") == "有" and input("你有车子吗?") == "有")

# 与运算  and   并且关系
# 现象:一假俱假 ,有一个不满足,结果就不满足
# 总结:"都得满足"
print(True and True)  # True 满足
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# 　命题：有钱　 或   有房
# print(input("你有钱吗?") == "有" or input("你有房吗?") == "有")
# input("你有钱吗?") == "有"
# input("你有房吗?") == "有"
# 或运算  or   或者关系
print(True or True)  # True 满足
print(True or False)  # True 满足
print(False or True)  # True 满足
print(False or False)  # False

# 非 -- 反转
print(not True)  # False

print(not False)  # True
