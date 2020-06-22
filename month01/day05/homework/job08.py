"""
10. 在终端中录入3个疫情省份的确诊人数
    最后打印最大值、最小值、平均值.（使用内置函数实现）
    内置函数:
    --max(x)	返回序列的最大值元素
    --min(x)	返回序列的最小值元素
    --sum(x)	返回序列中所有元素的和(元素必须是数值类型)
@author hailin
@date 2020-05-07
"""
# 定义空列表
number_of_confirmed = []
for i in range(3):
    number_of_confirmed.append(int(input("输入确诊人数为:")))

# 打印最大值、最小值、平均值
print("最大值:"+str(max(number_of_confirmed)))
print("最小值:"+str(min(number_of_confirmed)))
print("平均值:"+str(sum(number_of_confirmed) // len(number_of_confirmed)))

