"""
    字面值:表面的写法
        小数：1.5   1*e-5
        整数：10    0b10    0x10
        字符串:
"""
# 单引号　
str02 = '悟空'
# 双引号
str01 = "悟空"
# 三引号:可见即所得(注释)
str03 = '''悟空'''
str03 = """悟空"""

print("""
        *       *
        **     **
        ***   ***
        **** ****
""")

# 1.	单引号内的双引号不算结束符
# 2.	双引号内的单引号不算结束符
message = "我叫'祁天暄'."
message = '我叫"祁天暄".'
message = '''xx"xx"xxx'xxx'xxxxx'''

# 转义字符:   \"   \'   \\    \n换行
message = "我叫\"祁天暄\"."
message = "我叫\n祁天暄."
print(message)
# url = "c:\a\b\c\d.txt" # 错误\a  \b　是其他转义字符
# url = "c:\\a\\b\c\d.txt"
url = r"c:\a\b\c\d.txt"
print(url)
