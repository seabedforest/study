"""
6. 彩票模拟器 双色球：
        红球：6个,1-33之间（包含）,不能重复
        蓝色：1个,1--16之间（包含）
    -- (2) 在终端中"购买"彩票(提示：号码已经存在,号码超过范围)
@author hailin
@date 2020-05-08
"""
import random

# 创建空列表
list_lottery = []
# basketball = random.randint(1, 16)
# red_ball = random.randint(1, 33)
# 获取6个不重复的红球
while len(list_lottery) < 6:
    red_ball = int(input("请输入第%d个红球号码: " % (len(list_lottery) + 1)))
    if red_ball in list_lottery:
        print("号码已经存在")
    elif red_ball <1 or red_ball>33:
        print("号码超过范围,红球为1~33")
    else:
        list_lottery.append(red_ball)
# 最后加上蓝球，并显示结果
while len(list_lottery) < 7:
    basketball = int(input("请输入个蓝球号码:"))
    if basketball < 1 or basketball > 16:
        print("号码超过范围,蓝球为1~16")
    else:
        list_lottery.append(basketball)

print(list_lottery)