"""
彩票模拟器 双色球：
    红球：6个,1-33之间（包含）,不能重复
    蓝色：1个,1--16之间（包含）
@author hailin
@date 2020-05-08
"""
import random

# 创建空列表
numbers_lottery = []
numbers_lottery_buy = []
count = 0
# basketball = random.randint(1, 16)
# red_ball = random.randint(1, 33)
# 获取6个不重复的红球
while True:
    while len(numbers_lottery) < 6:
        red_ball = random.randint(1, 33)
        if red_ball not in numbers_lottery:
            numbers_lottery.append(red_ball)

    basketball = random.randint(1, 16)
    numbers_lottery.append(basketball)

    while len(numbers_lottery_buy) < 6:
        red_ball_buy = random.randint(1, 33)
        if red_ball_buy not in numbers_lottery_buy:
            numbers_lottery_buy.append(red_ball_buy)

    basketball_buy = random.randint(1, 16)
    numbers_lottery_buy.append(basketball_buy)
    count += 1
    if numbers_lottery == numbers_lottery_buy:
        print(f"这期中奖号码是{numbers_lottery}")
        print(f"第{count}次随机投注，你的投注彩票号码为{numbers_lottery_buy}，恭喜你中一等奖了")
        break
    else:
        print(f"这期中奖号码是{numbers_lottery}")
        numbers_lottery = []
        print(f"第{count}次随机投注，你的投注彩票号码为{numbers_lottery_buy},可惜你没有中奖")
        numbers_lottery_buy = []
