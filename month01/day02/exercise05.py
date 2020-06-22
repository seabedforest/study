"""
    从下列信息提取变量(注意数据的类型)
    在终端中为变量赋值
    再按照格式输出信息(注意类型的转换)
"""
# str --> 其他类型
price = float(input("请输入单价:"))
message = input("请输入介绍：")
review_count = int(input("请输入评论数："))

# .....

# 其他类型 --> str
print("￥" + str(price))
print(message)
print(str(review_count) + "条评价")

