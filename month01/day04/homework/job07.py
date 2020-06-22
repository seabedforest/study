"""
7. 赌大小游戏
    玩家的身家初始10000，实现下列效果：
        少侠请下注: 30000
        超出了你的身家，请重新投注。
        少侠请下注: 8000
        你摇出了5点,庄家摇出了3点
        恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩18000
        少侠请下注: 18000
        你摇出了6点,庄家摇出了6点
        打平了，少侠，在来一局？
        少侠请下注: 18000
        你摇出了4点,庄家摇出了6点
        少侠,你输了，身家还剩 0
        哈哈哈，少侠你已经破产，无资格进行游戏
@author hailin
@date 2020-05-06
"""
import random

asset = 10000
while True:
    jetton = int(input("少侠请下注:"))
    if jetton > asset:
        print("超出了你的身家，请重新投注")
        continue
    you_value = random.randint(1, 6)
    banker_value = random.randint(1, 6)
    if you_value > banker_value:
        asset += jetton
        print("恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩%d" % asset)
    elif you_value < banker_value:
        asset -= jetton
        print("少侠,你输了，身家还剩%d" % asset)
        if asset == 0:
            print("哈哈哈，少侠你已经破产，无资格进行游戏")
            break
    else:
        print("打平了，少侠，在来一局？")
