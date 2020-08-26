import numpy as np
import pandas as pd


#加载数据
data = pd.read_csv('./保健品问卷数据/保健品.csv')
#data.info()
print(data.describe())