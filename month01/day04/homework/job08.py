"""
8. (选做)一个小球从100m高度落下,每次弹回原高度一半.
   计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)
    -- 全过程总共移动多少米?
   提示:
       数据/操作
@author hailin
@date 2020-05-06
"""
metter = 100
trajectory = 100
count = 0
# upspring = 0
while True:
    metter /= 2
    count += 1
    if metter < 0.01:
        break
    trajectory += metter * 2
print("总共弹起%d次,全过程总共移动%.2f米"%(count,trajectory))