"""
numpy的数据类型
"""
import numpy as np

data = [
    ('zs', [90, 80, 85], 15),
    ('ls', [92, 81, 83], 16),
    ('ww', [95, 85, 95], 15)
]
# 第一种设置dtype的方式
ary = np.array(data, dtype='U2,3int32,int32')
print(ary)
print(ary[0])
print(ary['f1'])
print('*' * 50)
# 第二种设置dtype的方式
ary2=np.array(data, dtype=[('name', 'str', 2), ('scores', 'int32', 3), ('age', 'int32', 1)])
print(ary2)
print(ary2['name'])
print('*' * 50)
#第三种设置dtype的方式
ary3 = np.array(data,dtype={'names':['name','scores','age'],'formats':['U2','3int32','int32']})
print(ary3[1]['age'])

# 测试日期数据
f = np.array(['2011','2012-01-01','2013-01-01 01:01:01','2011-02-01'])
dates= f.astype('M8[D]')
print(dates,dates.dtype)
d=dates[0]-dates[1]
print(d,type(d))