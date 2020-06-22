"""
    if 语句的真值表达式
        if 值: # bool(值)
            满足条件的代码
"""
content = input("请输入文字:")
# content如果有值
if content:  # if bool(content):
    print("您输入的是" + content)
