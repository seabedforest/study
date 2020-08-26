"""
Series对象
"""
import numpy as np
import pandas as pd

# 创建Series对象
ary = np.array(['zs', 'ls', 'ww', 'zl'])
# 使用index参数可以更改索引
s = pd.Series(ary, index=['s01', 's02', 's03', 's04'])
# print(s)
# # 使用字典创建Series
# s = pd.Series({'s01': 'zs', 's02': 'ls', 's03': 'ww'})
# print(s)
#
# # 使用标量创建Series
# s = pd.Series(5, index=[0, 1, 2, 3, 4])
# print(s)

# Series的访问
# print(s[1], ['s02'])
# print(s[1:3])
# print(s['s02':'s03'])
# mask = [True, False, False, True]
# print(s[mask])
# print(s[[0, 2]])
# print(s[['s02', 's04']])

#四个元素倒序输出
# print(s[::-1])
# print(s[[3,2,1,0]])
# print(s[['s04','s03','s02','s01']])
# print(s.index)
# print(s.values)


# pandas识别的日期字符串格式
dates = pd.Series(['2011', '2011-02', '2011-03-01', '2011/04/01',
                   '2011/05/01 01:01:01', '01 Jun 2011'])

dates=pd.to_datetime(dates)
print(dates)
delta = dates - pd.to_datetime('20110101')
print(delta)
#