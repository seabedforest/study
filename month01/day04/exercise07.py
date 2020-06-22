"""
循环录入编码值,打印文字.直到输入空字符串,停止。
21016
28023
26519
"""
while True:
    code_value = input("输入编码值:")
    if code_value == "":
        break
    word = chr(int(code_value))
    print(word)