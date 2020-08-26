"""
属性测试
"""
import numpy as np

a=np.arange(1,13)
print(a,a.shape)

#视图变维
b=a.reshape(2,6)
a[0]=999
print(b)
print(b.ravel())
#复制变维
c=a.flatten()
a[2]=998
print(c)