"""
    字符串编码
	ord(字符串):返回该字符串的Unicode码。
	chr(整数):返回该整数对应的字符串。
	练习:exercise06
"""
# 字　　-编码->  　数
code_value = ord("祁")
print(code_value)  # 31041

# 数(十进制)　　-解码->  　字
char = chr(31041)
print(char)
