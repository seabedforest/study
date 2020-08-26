# 列的访问
import numpy as np
import pandas as pd

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([1, 3, 4], index=['a', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print(df[['one', 'two']])
print('*' * 40)
print(df[df.columns[:-1]])
print('*' * 40)
# 复合索引
# 生成一组(6,3)的随机数。要求服从期望=85,标准差=3的正态分布
data = np.floor(np.random.normal(85, 3, (6, 3)))
df = pd.DataFrame(data)
print(df)
# 设置行级标签索引为复合索引
index = [('A', 'M'), ('A', 'F'), ('B', 'M'), ('B', 'F'), ('C', 'M'), ('C', 'F')]
df.index = pd.MultiIndex.from_tuples(index)
print(df)
columns = [('score', 'math'), ('score', 'reading'), ('score', 'writing')]
df.columns = pd.MultiIndex.from_tuples(columns)
print(df)
# C班男生的信息
print(df.loc['C', 'M'])

print(df.loc[['A','C']])
print('*' * 40)
#访问复合索引列
print(df['score','writing'])