"""
共享单车数据分析
"""
import numpy as np

# 加载数据
with open('./bike_day.csv', 'r') as f:
    data = []
    for i, line in enumerate(f.readlines()):
        if i == 0:
            header = line[:-1].split(',')
        else:
            data.append(tuple(line[:-1].split(',')))

# 把data转成ndarray
ary = np.array(data, dtype={'names': header, 'formats': ['i4', 'U15', 'i4', 'i4', 'i4',
                                                         'i4', 'i4', 'i4', 'i4', 'f8',
                                                         'f8', 'f8', 'f8', 'i4', 'i4', 'i4']})

# print(ary)
print(ary['holiday'].sum())
# 输出前10行数据
print(ary[:10])
# 获取周一的数据
print(ary[ary['weekday'] == 1])
# 求 节假日天数的占比  holiday
holidays = ary[ary['holiday'] == 1]
print(len(holidays) / len(ary))
