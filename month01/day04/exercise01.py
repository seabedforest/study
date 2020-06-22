"""
程序产生一个1到100之间的随机数。让玩家重复猜测,直到猜对为止。每次提示：大了、小了、恭喜猜对了,总共猜了多少次。
@author hailin
@date 2020-05-06
"""
# 1. 随机数工具
import random
# 2. 产生随机数
random_number = random.randint(1, 100)
count = 1
while True:
    num02 = int(input("输入一个1到100的数字:"))
    if random_number > num02:
        print("小了")
    elif random_number < num02:
        print("大了")
    else:
        print("恭喜猜对了,"+"总共猜了"+str(count)+"次")
        break
    count += 1
