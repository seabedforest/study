"""
    for 循环 -- 遍历
    练习:exercise02
"""
message = "1234"
for item in message:
    print(item)

for item in message:
    item = ""  # 修改的是变量item,不影响变量message,更不影响字符串 "我是齐天大圣"

print(message)  # "我是齐天大圣"
