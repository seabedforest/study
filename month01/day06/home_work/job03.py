"""
6. 彩票模拟器 双色球：
        红球：6个,1-33之间（包含）,不能重复
        蓝色：1个,1--16之间（包含）
    -- (1) 创建随机彩票(一个列表,前六个是红球,最后一个是蓝球)    考点:如何产生多个不重复的随机数
    -- (2) 在终端中"购买"彩票(提示：号码已经存在,号码超过范围)
    -- (3) ..玩..
@author hailin
@date 2020-05-08
"""
import random

# (1) 创建随机彩票(一个列表,前六个是红球,最后一个是蓝球)
# 创建空列表
list_lottery = []
basketball = random.randint(1, 16)

# 随机获取6个不重复的红球
while len(list_lottery) < 6:
    red_ball = random.randint(1, 33)
    if red_ball not in list_lottery:
        list_lottery.append(red_ball)
# 最后加上蓝球，并显示结果
list_lottery.append(basketball)
print(list_lottery)
