"""
5. 将列表中所有元素转换为一个字符串
   列表:["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
   结果:我爱你python666
@author hailin
@date 2020-05-08
"""
# 列表数据
words = ["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]

string = "".join([str(char) for char in words])
# 显示结果
print(string)
