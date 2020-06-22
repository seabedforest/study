"""
根据下列代码,定义函数,获取课程阶段名称.
number_of_stage = input("输入课程阶段数:")
if number_of_stage == "1":
print("Python语言核心编程")
elif number_of_stage == "2":
print("Python高级软件技术")
elif number_of_stage == "3":
print("Web 全栈")
elif number_of_stage == "4":
print("网络爬虫")
elif number_of_stage == "5":
print("数据分析、人工智能")
else:
print("输入有误")
"""
def get_course_title(number_of_stage):
    """
    获取课程名称
    :param number_of_stage: 课程阶段
    :return: 课程名称
    """
    dict_course = {
    "1": "Python语言核心编程",
    "2": "Python高级软件技术",
    "3": "Web 全栈",
    "4": "网络爬虫",
    "5": "数据分析、人工智能"
    }
    # 如果课程编号存在,则返回字典值, 否则返回None,表示不存在该课程
    return dict_course[number_of_stage] if number_of_stage in dict_course else None

# 测试
title = get_course_title("1")
if title: #
    print("课程名称是" + title)
else:
    print("输入有误")