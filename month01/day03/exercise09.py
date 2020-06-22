"""
    核心:判断数值,在一个连续的区间范围内
"""
# ma = int(input("心里年龄："))
# ca = int(input("实际年龄："))
# intelligence = ma / ca * 100
# if intelligence >= 140:
#     print("天才")
# elif 120 <= intelligence <= 139:
#     print("超常")
# elif 110 <= intelligence <= 119:
#     print("聪慧")
# elif 90 <= intelligence < 109:
#     print("正常")
# elif 80 <= intelligence <= 89:
#     print("迟钝")
# else:
#     print("低能")

# 建议
mental_age = int(input("心理年龄："))
real_age = int(input("真实年龄："))
iq = mental_age / real_age * 100
if iq >= 140:
    print("天才")
elif iq >= 120: # 小于140
    print("超常")
elif iq >= 110:
    print("聪慧")
elif iq >= 90:
    print("正常")
elif iq >= 80:
    print("迟钝")
elif iq < 80:
    print("低能")
